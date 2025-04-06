import torch
import torch.nn as nn
import math



# def generate_layer_code2(layer_index: int, layer: nn.Linear) -> str:
#     code_lines = []

#     # Branch if Relu.
#     if isinstance(layer, nn.ReLU):
#         # ignore.
#         # we have the relu's covered in the perceptron code.
#         return ""
    
#     # generate the layer function
#     code_lines.append(f"def l{layer_index}_(x):")
#     code_lines.append("    # x is a list (or vector) of length {}".format(layer.weight.shape[1]))
    
#     # add each term from a perceptron
#     perceptron_vars = []
#     for i in range(layer.weight.shape[0]):
#         # perceptron_code = generate_perceptron_code2(layer_index, layer, i)
#         linear_expr = generate_perceptron_code2(layer_index, layer, i)
#         perceptron_vars.append(f"p{i}")
#         code_lines.append(f"    {perceptron_vars[i]} = ({linear_expr})")
    
#     code_lines.append("    return [")
#     code_lines.append("        " + " + ".join(perceptron_vars) + ",")
    
#     # for i in range(layer.weight.shape[0]):
#         # code_lines.append(f"        l{layer_index}_{i}(x),")
    
#     code_lines.append("    ]")
    
#     return "\n".join(code_lines)

# def generate_perceptron_code2(layer_index: int, linear_layer: nn.Linear, neuron_index: int) -> str:
#     # Extract weights and bias for the given neuron
#     weights = linear_layer.weight.data[neuron_index].tolist()
#     bias = linear_layer.bias.data[neuron_index].item() if linear_layer.bias is not None else 0.0
    
#     # Construct the linear combination string
#     terms = []
    
#     # Add bias if nonzero
#     if abs(bias) > 1e-6:
#         terms.append(f"{bias}")
    
#     for i, w in enumerate(weights):
#         if abs(w) > 1e-6:
#             terms.append(f"{w}*x[{i}]")
    
#     # Join the terms; if none, default to bias=0
#     linear_expr = " + ".join(terms) if terms else "0"
    
#     return linear_expr
    
#     # Wrap with ReLU (i.e. max(0, ...))
#     # code_lines.append(f"    return max(0, {linear_expr})")
#     # code_lines.append(f"    return ({linear_expr})")










def generate_layer_code(layer_index: int, layer: nn.Linear) -> str:
    code_lines = []

    # Branch if Relu.
    if isinstance(layer, nn.ReLU):
        # ignore.
        # we have the relu's covered in the perceptron code.
        return ""
    
    for i in range(layer.weight.shape[0]):
        perceptron_code = generate_perceptron_code(layer_index, layer, i)
        code_lines.append(perceptron_code)
    
    # generate the layer function
    code_lines.append(f"def l{layer_index}_(x):")
    code_lines.append("    # x is a list (or vector) of length {}".format(layer.weight.shape[1]))
    code_lines.append("    return [")
    for i in range(layer.weight.shape[0]):
        code_lines.append(f"        l{layer_index}_{i}(x),")
    code_lines.append("    ]")
    
    return "\n".join(code_lines)

def generate_perceptron_code(layer_index: int, linear_layer: nn.Linear, neuron_index: int) -> str:
    print(f"weights: {linear_layer.weight.data[neuron_index]}")
    print(f"bias: {linear_layer.bias.data[neuron_index]}")
    
    # Extract weights and bias for the given neuron
    weights = linear_layer.weight.data[neuron_index].tolist()
    bias = linear_layer.bias.data[neuron_index].item() if linear_layer.bias is not None else 0.0
    
    # Build the function string header
    code_lines = []
    code_lines.append(f"def l{layer_index}_{neuron_index}(x):")
    code_lines.append("    # x is a list (or vector) of length {}".format(len(weights)))
    
    # Construct the linear combination string
    terms = []
    
    notes = ""
    
    # Add bias if nonzero
    # check if bias is not integer when converted from float.
    if bias not in [0.0]:
        terms.append(f"{bias}")
    
    flagged_set = []
    flagged_not = []
    bitshift_set = []
    
    for i, w in enumerate(weights):
        # print(int(-1 * w))
        # print(type(int(abs(w))))
        
        # interp.
        if w in [0.0]:
            flagged_not.append(i)
        elif w in [1.0]:
            flagged_set.append(i)
        # bitshift format:
        # x << n = 2^n * x
        # x >> n = -2^n * x
        # detect if w (n) is a power of 2 log2(w) is an integer.
        elif math.log2(int(abs(w))) % 1 == 0:
            w2 = int(w)
            # bitshift_dirs = ["<<", ">>"]
            # get the sign of w
            bitshift = "<<" if w2 > 0 else ">>"
            # compute log2(w) to get factor
            factor = math.log2(abs(w2))
            bitshift_set.append(f"x[{i}] {bitshift} {factor}")
        
        # output.
        if w in [1.0]:
            terms.append(f"x[{i}]")
        elif w in [0.0]:
            terms.append(f"x[{i}]")
        else:
            terms.append(f"{w}*x[{i}]")
    
    linear_expr = ""
    
    # INTERP COMMENTS.
    # 
    
    
    # 1) masks
    # flagged 111100001110011 for the entire len of x, 0 or 1 based on flagged_set or flagged_not, and ? for weights that aren't included
    flag_comment = "    # masks "
    for i in range(len(weights)):
        if i in flagged_set:
            flag_comment += "1"
        elif i in flagged_not:
            flag_comment += "0"
        else:
            flag_comment += "?"
    code_lines.append(flag_comment)
    
    # 2) bitshifts
    bitshift_comment = "    # bitshifts"
    for bitshift in bitshift_set:
        bitshift_comment += f"    {bitshift}"
    code_lines.append(bitshift_comment)
    
    # 3) linear combination
    """
    def l6_139(x):
        # x is a list (or vector) of length 64
        # flagged 0001000000000000000000000000000000000000000000000000000000000000
        # bitshifts
        return max(0, -127.0 + x[3])
    """
    # this look like:
    # abs(w) is factor of 2 minus something
    # 
    
    
    # Join the terms; if none, default to bias=0
    linear_expr += " + ".join(terms) if terms else "0"
    
    # Wrap with ReLU (i.e. max(0, ...))
    code_lines.append(f"    return max(0, {linear_expr})")
    # code_lines.append(f"    return ({linear_expr})")
    
    # Join all lines into a single code string
    return "\n".join(code_lines)




model = torch.load("js.pt", weights_only=False, map_location='cpu')

# We are going to do this.
# output to analysis/layers/l[index].py each layer.
i = 6
j = 22
layer = model[i]

if isinstance(layer, nn.ReLU):
    # ignore. we cover these in the perceptron code.
    exit()

# print(generate_layer_code(i, layer))
print(generate_perceptron_code(i, layer, j))
