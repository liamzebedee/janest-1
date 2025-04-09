

import torch
from onnxsim import simplify
import onnx
import copy
import torch.nn as nn

# Returns:
#     str: The Python code representing the model definition.
def generate_code(model):
    from torch import nn
    
    # Write out the model definition as Python code.
    # import torch
    # from torch import nn
    # class JSModel(nn.Module):
    #     def __init__(self):
    #         super(JSModel, self).__init__()
    #         self.layer1 = nn.Linear(55, 224)
    #         self.layer2 = nn.ReLU()
    #         self.layer3 = nn.Linear(224, 232)
    #         self.layer4 = nn.ReLU()
    #         ...
    #         for i, layer in enumerate(model):
    # 
    #    def forward(self, x):
    #        for layer in model:
    #            x = layer(x)
    #        return x
    # Write out the model definition as Python code.
    
    layer_defs = ""
    for i, layer in enumerate(model):
        # switch on layer type
        if isinstance(layer, nn.Linear):
            layer_defs += f"            nn.Linear({layer.in_features}, {layer.out_features}, bias=True)"
        elif isinstance(layer, nn.ReLU):
            layer_defs += f"            nn.ReLU()"
        else:
            raise ValueError(f"Unknown layer type: {type(layer)}")
        if i < len(model) - 1:
            layer_defs += f",\n"

    model_code = f"""
import torch
from torch import nn

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.layers = nn.Sequential(*[
{layer_defs}
        ])

    def forward(self, x):
        return self.layers(x)
"""
    return model_code


def check_onnx():
    import onnx
    onnx_model = onnx.load("js.onnx")
    print(onnx_model)
    print("Inputs:", [inp.name for inp in onnx_model.graph.input])
    print("Outputs:", [out.name for out in onnx_model.graph.output])


def inst_code(code):
    n = {}
    exec(code, n, n)
    Model = n["Model"]
    return Model()

def apply_state_dict(model_orig, model):
    # Generate state dict for the model.
    new_state_dict = {}
    for key, value in model_orig.state_dict().items():
        new_key = f"layers.{key}"  # Add 'model.' to the key name to match the new model's format
        new_state_dict[new_key] = value
    
    # put the weights from the original model into the new model
    model.load_state_dict(new_state_dict)
    model.eval()
    
    # test with an input
    input = torch.randn(1, 55)
    output = model(input)
    print(output)
    
    return model


d= """

"""


def generate_properties(model, n_inputs, n_outputs):
    l = []
    print("n_inputs:", n_inputs)
    print("n_outputs:", n_outputs)
    
    for i in range(n_inputs):
        l.append(f"x{i} >= 0\n")
        l.append(f"x{i} <= 1\n")
        
    # # Hidden layer bounds
    # for layer_idx, layer in enumerate(model.layers):
    #     if isinstance(layer, nn.Linear):
    #         # Assume fully connected layers (nn.Linear)
    #         num_neurons = layer.weight.shape[0]  # Output dimension of the layer
    #         for neuron_idx in range(num_neurons):
    #             # Use h_layerIndex_nodeIndex syntax
    #             l.append(f"h_{layer_idx}_{neuron_idx} >= 0\n")
    #             l.append(f"h_{layer_idx}_{neuron_idx} <= 1\n")
    
    # Hidden layer bounds (target ReLU outputs)
    prev_linear_output_size = n_inputs  # Initial input size
    for layer_idx, layer in enumerate(model.layers):
        if isinstance(layer, nn.Linear):
            # Store the output size for the next ReLU
            prev_linear_output_size = layer.weight.shape[0]
        elif isinstance(layer, nn.ReLU):
            # Bound the ReLU outputs
            num_neurons = prev_linear_output_size  # Matches the Linear output feeding into this ReLU
            for neuron_idx in range(num_neurons):
                # l.append(f"h_{layer_idx}_{neuron_idx} <= 256.0\n")
                # l.append(f"h_{layer_idx}_{neuron_idx} >= -256.0\n")
                # l.append(f"h_{layer_idx}_{neuron_idx} <= -1\n")
                # l.append(f"h_{layer_idx}_{neuron_idx} >= 1\n")
                pass
    
    l.append("y0 = 1\n")
    return "".join(l)

if __name__ == "__main__":
    # Original model, without implementation, only weights + architecture metadata.
    print("loading model")
    model_orig = torch.load("../../js.pt", weights_only=False, map_location='cpu')
    
    # Realised model, with code.
    model = inst_code(generate_code(model_orig))
    model = apply_state_dict(model_orig, model)
    
    # Slice model down.
    slice_start = 5432
    experiment_name = f"js_{slice_start}"
    model.layers = model.layers[slice_start:]
    
    # Test the model (sanity check).
    input_tensor = torch.randn(1, *model.layers[0].weight.shape[1:])
    # do a test predict
    output = model(input_tensor)
    print("number of layers:", len(model.layers))
    print("input shape:", input_tensor.shape)
    print("output shape:", output.shape)
    
    # Export onxx.
    print("exporting onxx")
    onxx_model_file = f"{experiment_name}.onnx"
    torch.onnx.export(
        model,
        input_tensor,
        onxx_model_file,
        input_names=["input"],
        output_names=["output"],
        opset_version=11,
    )
    
    print("simplifying (onxxsimp)")
    model_onxx = onnx.load(onxx_model_file)
    model_onxx_simp, check = simplify(model_onxx)
    assert check, "Simplified ONNX model could not be validated"

    # export simplified model.
    print("exporting onxx-simpl")
    onnx.save(
        copy.deepcopy(model_onxx_simp),
        f"{experiment_name}.onnxsim.onnx",
    )
    
    # import code
    # code.interact(local=locals())
    
    # create properties to solve for.
    properties_data = generate_properties(model, input_tensor.shape[1], output.shape[1])
    with open(f"{experiment_name}.properties.txt", "w") as f:
        f.write(properties_data)
    
    # output SMT solver command
    MARABOU_BIN = "/Users/liamz/Documents/Research/2025-ml/pytorch-exps/js/Marabou/build/bin/Marabou"
    print("SMT solver command:")
    print(f"{MARABOU_BIN} {experiment_name}.onnx {f'{experiment_name}.properties.txt'} --num-workers=8 --verbosity=1 --milp")
    # print(f"{MARABOU_BIN} {experiment_name}.onnxsim.onnx {f'{experiment_name}.properties.txt'} --milp --num-workers=8 --verbosity=1")
    print("")
    
    print("done")
    
    
    