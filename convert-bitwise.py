import torch
import torch.nn as nn

def generate_layer_code(layer_index: int, layer: nn.Linear) -> str:
    code_lines = []

    # Branch if Relu.
    if isinstance(layer, nn.ReLU):
        code_lines.append(f"def l{layer_index}(x):")
        # apply max(0, x) to each element.
        code_lines.append("    return [max(0, x[i]) for i in range(len(x))]")
        return "\n".join(code_lines)
    
    for i in range(layer.weight.shape[0]):
        perceptron_code = generate_perceptron_code(layer_index, layer, i)
        code_lines.append(perceptron_code)
    
    # generate the layer function
    code_lines.append(f"def l{layer_index}(x):")
    code_lines.append("    # x is a list (or vector) of length {}".format(layer.weight.shape[1]))
    code_lines.append("    return [")
    for i in range(layer.weight.shape[0]):
        code_lines.append(f"        l{layer_index}_{i}(x),")
    code_lines.append("    ]")
    
    return "\n".join(code_lines)

def generate_perceptron_code(layer_index: int, linear_layer: nn.Linear, neuron_index: int) -> str:
    # Extract weights and bias for the given neuron
    weights = linear_layer.weight.data[neuron_index].tolist()
    bias = linear_layer.bias.data[neuron_index].item() if linear_layer.bias is not None else 0.0
    
    # Build the function string header
    code_lines = []
    code_lines.append(f"def l{layer_index}_{neuron_index}(x):")
    code_lines.append("    # x is a list (or vector) of length {}".format(len(weights)))
    
    # Construct the linear combination string
    terms = []
    # Add bias if nonzero
    if abs(bias) > 1e-6:
        terms.append(f"{bias}")
    for i, w in enumerate(weights):
        if abs(w) > 1e-6:  # only include significant terms
            terms.append(f"{w}*x[{i}]")
    
    # Join the terms; if none, default to bias=0
    linear_expr = " + ".join(terms) if terms else "0"
    
    # Wrap with ReLU (i.e. max(0, ...))
    code_lines.append(f"    return max(0, {linear_expr})")
    
    # Join all lines into a single code string
    return "\n".join(code_lines)

# Example usage:

model = torch.load("js.pt", weights_only=False, map_location='cpu')

# Create a sample linear layer with 232 inputs and 64 outputs.
layer = model[4]


print(generate_layer_code(4, layer))

# We are going to do this.
# output to analysis/layers/l[index].py each layer.

for i in range(len(model)):
    layer = model[i]
    with open(f"analysis/layers/l{i}.py", "w") as f:
        f.write(generate_layer_code(i, layer))
