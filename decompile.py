import torch
import torch.nn as nn
import math


def generate_layer_code(layer_index: int, layer: nn.Linear) -> str:
    code_lines = []

    # Branch if Relu.
    if isinstance(layer, nn.ReLU):
        # ignore.
        # we have the relu's covered in the perceptron code.
        return ""
    
    # generate perceptron full function (decompiled)
    decompiled_layer_fn = decompile_layer_fn(layer_index, layer)
    if len(decompiled_layer_fn) > 0:
        code_lines.append("import numpy as np\n\n")
        code_lines.append("\n")
        code_lines.append(decompiled_layer_fn)
        code_lines.append("\n")
    
    # generate perceptron full function (reduce)
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
    
    return "\n".join(code_lines), decompiled_layer_fn

def generate_perceptron_code(layer_index: int, linear_layer: nn.Linear, neuron_index: int) -> str:
    # Extract weights and bias for the given neuron
    weights = linear_layer.weight.data[neuron_index].tolist()
    wd = linear_layer.weight.data[neuron_index] # weight data
    bias = linear_layer.bias.data[neuron_index].item() if linear_layer.bias is not None else 0.0
    
    # Build the function string header
    code_lines = []
    code_lines.append(f"def l{layer_index}_{neuron_index}(x):")
    code_lines.append("    # x is a list (or vector) of length {}".format(len(weights)))
    
    # Construct the linear combination string
    terms = []
    
    for i, w in enumerate(weights):
        # print(int(-1 * w))
        # print(type(int(abs(w))))
        # print()
        
        # output.
        if w in [1.0]:
            terms.append(f"x[{i}]")
        elif w in [0.0]:
            # weight for this bit is 0.
            # hence we do not need to capture it.
            pass
        else:
            terms.append(f"{w}*x[{i}]")
    
    # INTERP COMMENTS.
    # 
    interp_lines = []
    flag_add = list("0" * len(weights))
    flag_sub = list("0" * len(weights))
    flag_zero = list("0" * len(weights))
    bitshift_set = []
    other_terms = []
    
    
    for i, w in enumerate(weights):
        if w in [0.0]:
            flag_zero[i] = "1"
        elif w in [1.0]:
            flag_add[i] = "1"
        elif w in [-1.0]:
            flag_sub[i] = "1"
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
            # check factor has decimal
            if factor % 1 != 0:
                raise Exception(f"factor: {factor}")
            
            bitshift_set.append(f"x[{i}] {bitshift} {int(factor)}")
        else:
            other_terms.append(f"{w}*x[{i}]")
            
    
    # 1) masks
    # flagged 111100001110011 for the entire len of x, 0 or 1 based on flagged_set or flagged_not, and ? for weights that aren't included
    flag_comment = "    # masks "
    flag_comment += f"    # add: {''.join(flag_add)}"
    flag_comment += f"    # sub: {''.join(flag_sub)}"
    flag_comment += f"    # zero: {''.join(flag_zero)}"
    interp_lines.append(flag_comment)
    
    # 2) bitshifts
    bitshift_comment = "    # bitshifts"
    for bitshift in bitshift_set:
        bitshift_comment += f"    {bitshift}"
    interp_lines.append(bitshift_comment)
    # push to code_lines
    for line in interp_lines:
        # code_lines.append(line)
        pass
    
    
    # Add bias if nonzero
    # check if bias is not integer when converted from float.
    if bias not in [0.0]:
        terms.append(f"{bias}")
    
    linear_expr = ""
    # Join the terms; if none, default to bias=0
    linear_expr += " + ".join(terms) if terms else "0"
    
    # Wrap with ReLU (i.e. max(0, ...))
    code_lines.append(f"    return max(0, {linear_expr})")
    
    # Join all lines into a single code string
    return "\n".join(code_lines)

import numpy as np


def binarray_to_hex(arr):
    # Convert the array of 1.0/0.0 into a string of bits.
    bits = ''.join('1' if x else '0' for x in arr)
    # Convert the bit string to an integer.
    n = int(bits, 2)
    # Calculate the number of hex digits needed (each hex digit represents 4 bits).
    num_hex_digits = (len(arr) + 3) // 4
    # Format the integer into a zero-padded hex string.
    return format(n, '0{}x'.format(num_hex_digits))


# reverse engineering.
def decompile_layer_fn(layer_index: int, la: nn.Linear):   
    DEBUG = False
     
    # weight data
    wd = la.weight.data
    # bias data
    bd = la.bias.data
    
    # weight patterns
    wps = [wd[0]]
    # start indices of each weight pattern
    starts = [0]
    # biases
    bss = []
    
    # 1. iterate over perceptrons.
    for i in range(la.weight.shape[0]):
        bias = la.bias.data[i].item() if la.bias is not None else 0.0
        bss.append(bias)
        
        # Weight pattern is when wd is just prev elements shifted right by 1
        a = wps[-1]
        b = wd[i]
        
        # if i == 57 or i == 58:
        #     print(a)
        #     print(b)
        #     continue
        
        is_same_pattern = torch.all(b == torch.roll(a, i - starts[-1]))
        if DEBUG:
            print("pattern", f"unit#{i:2d}", f"pattern#{len(wps):1d}", bias)
        
        if not is_same_pattern:
            # found a new pattern
            wps.append(wd[i])
            starts.append(i)
    
    if starts[-1] != len(wd):
        starts.append(len(wd))
        
    # exit(0)
    # print(starts)
    
    code_lines = []
    code_lines.append("# Generated from reverse engineering")
    code_lines.append(f"def l{layer_index}_g(x: np.ndarray) -> np.ndarray:")
    code_lines.append(f"    # x is a list (or vector) of length {len(wd)}")
    code_lines.append(f"    out = np.empty({la.weight.shape[0]}, dtype=np.float32)")
    code_lines.append(f"    ")
    
    # generate perceptron pseudocode
    for wi, ws in enumerate(wps):
        # code_lines.append(f"    # pattern {i:2d}  starts={starts[i]:3d} ends={starts[i+1]:3d}\n")
        # w_str = str(w)
        # pseudocode += f"#{i} {starts[i]} {w_str}\n"
        # now we have the patterns.
        # we can construct code from them.
        
        # start bit
        sb = starts[wi]
        # end bit
        eb = starts[wi+1] - 1
        # print(sb)
        
        """
        A tutorial on re-rolling loops:
        
        def l4_0(x):
            # x is a list (or vector) of length 232
            # masks 10000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000000000000000000000000000
            # bitshifts    x[56] << 7    x[112] >> 8    x[168] << 7
            # weight sections

            return max(0, x[0] + 128.0*x[56] + -256.0*x[112] + 128.0*x[168])
        def l4_1(x):
            # x is a list (or vector) of length 232
            # masks 010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000000000000000000000000000
            # bitshifts    x[57] << 7    x[113] >> 8    x[169] << 7
            # weight sections

            return max(0, x[1] + 128.0*x[57] + -256.0*x[113] + 128.0*x[169])
        def l4_2(x):
            # x is a list (or vector) of length 232
            # masks 0010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000000000
            # bitshifts    x[58] << 7    x[114] >> 8    x[170] << 7
            # weight sections

            return max(0, x[2] + 128.0*x[58] + -256.0*x[114] + 128.0*x[170])
            
        There are three neuron defintions above.
        Each neuron operates on a fixed number of bits (3).
        neuron 1 -  56 112 168
        neuron 2 -  57 113 169
        neuron 3 -  58 114 170
        
        made generic
        neuron i   -  j   k   l
        neuron i+1 -  j+1 k+i l+i
        neuron i+2 -  j+2 k+2 l+2
        ...
        neuron i+p -  j+p k+p l+p
        
        We know p=sb (start bit), q=eb (end bit)
        Our job is to output the expressions for the operations on each bit.
        
        3 expressions:
        x[i:p] << 7    x[i:p] >> 8    x[i:p] << 7
        
        x[56:112] << 7 + x[112:168] >> 8 + x[168:224] << 7
        
        
        
        Now coming to masks
        neuron i     10000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?000000000000000000000000000000000000000000000000000000000000000
        neuron i+1   010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?00000000000000000000000000000000000000000000000000000000000000
        neuron i+2   0010000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000?0000000000000000000000000000000000000000000000000000000000000
        """
        
        
        flagged_set = []
        flagged_not = []
        flagged_neg1 = []
        bitshift_set = []
        
        for i, w in enumerate(ws):
            if w in [0.0]:
                flagged_not.append(i)
            elif w in [1.0]:
                flagged_set.append(i)
            elif w in [-1.0]:
                flagged_neg1.append(i)
            # bitshift format:
            # x << n = 2^n * x
            # x >> n = -2^n * x
            # detect if w (n) is a power of 2 log2(w) is an integer.
            elif w not in [0.0, 1.0, -1.0] and math.log2(int(abs(w))) % 1 == 0:
                w2 = int(w)
                bitshift = "<<"
                sign = "" if w2 > 0 else "-"
                factor = math.log2(abs(w2))
                # check factor has decimal
                if factor % 1 != 0:
                    raise Exception(f"factor: {factor}")
                # bitshift_set.append(f"x[{sb+i}:{eb+i}] {bitshift} {int(factor)}")
                # bitshift_set.append(f"{sign}1*(x[i + {i}] {bitshift} {int(factor)})")
                
                # COOL.
                # bitshift_set.append(f"{sign}1*(x[i + {i}] {bitshift} {int(factor)})")
                
                # NORMAL
                bitshift_set.append(f"{w} * x[i + {i}]")
        
        # l4_56:
        # for i in range(56, 64):
        #     s = x[i + 168]
        #     out[i] = s if s > 0 else 0.0  # ReLU
        # print(flagged_set)
        
        masked_on = []
        for i in flagged_set:
            # masked_on.append(f"x[i + {i-sb}]")
            masked_on.append(f"x[{i} + i]")
        for i in flagged_neg1:
            # masked_on.append(f"-1 * (x[i + {i-sb}])")
            masked_on.append(f"-1 * x[{i} + i]")
            
        # s = x[i] + x[i + 56] << 7 + x[i + 112] >> 8 + x[i + 168] << 7
        # out[i] = s if s > 0 else 0.0  # ReLU
        terms = [] + masked_on + bitshift_set
        
        # Join the terms; if none, default to bias=0
        linear_expr = " + ".join(terms) if terms else "0"
        
        block_biases = bss[:][sb:eb+1]
        show_biases = not torch.all(torch.tensor(block_biases) == 0.0)
        
        # check if biases contain only 0 and or 1's
        is_binary_bias_vec = all(b in [0.0, 1.0] for b in block_biases)
        # if binary, convert to hex string and append as comment on top
        if is_binary_bias_vec and show_biases:
            # hex_biases = hex(int(''.join(list(map(str, list(map(int,block_biases))))),2))
            hex_biases = binarray_to_hex(block_biases)
            code_lines.append(f"    # biases: 0x{hex_biases} (len={len(block_biases)})")
        
        code_lines.append(f"    biases = {bss[:][sb:eb+1]}") if show_biases else ""
        code_lines.append(f"    # for i in range({sb}, {eb+1}):")
        code_lines.append(f"    for i in range(0, {eb - sb + 1}):")
        code_lines.append(f"        s = {linear_expr}")
        code_lines.append(f"        s += biases[i]") if show_biases else ""
        code_lines.append(f"        out[{sb} + i] = s if s > 0 else 0.0 # ReLu")
        code_lines.append(f"        ")
        
    
    code_lines.append(f"    return out")
    code_lines.append(f"")
    code_lines.append(f"")
    
    return "\n".join(code_lines)




# Example usage:
model = torch.load("js.pt", weights_only=False)

def write_layer(i: int, layer: nn.Linear):
    with open(f"analysis/layers2/l{i}.py", "w") as f:
        code = generate_layer_code(i, layer)
        f.write(code)



# li = 2
# layer = model[li]
# print(generate_layer_code(li, layer))
# write_layer(li, layer)
# print(decompile_layer_fn(li, layer))


def decompile_all_layers(model):
    # We are going to do this.
    # output to analysis/layers/l[index].py each layer.
    single_file = ""

    for i in range(len(model)):
        print(i)
        # stop at i == 50.
        
        # if i > 50:
        #     break
        
        layer = model[i]
        if isinstance(layer, nn.ReLU):
            # ignore. we cover these in the perceptron code.
            continue
        
        try:
            code, _ = generate_layer_code(i, layer)
            f = open(f"analysis/layers2/l{i}.py", "w")
            f.write(code)
            f.close()
        except Exception as e:
            print(e)
            exit()

    exit(0)
decompile_all_layers(model)

def dec_single_file(model):
    # Deecompile into single file single.py
    single_file = []
    debug_i = -1
    
    for i in range(len(model)):
        layer = model[i]
        print(i)
        
        if debug_i != -1 and i == debug_i:
            break
        
        layer = model[i]
        if isinstance(layer, nn.ReLU):
            # ignore. we cover these in the perceptron code.
            continue
        
        try:
            decompiled = decompile_layer_fn(i, layer)
            single_file.append(decompiled)
        except Exception as e:
            print("ex: "+ e)
            exit()

    single_file.insert(0, """
import numpy as np
import torch
    """)
    single_file.append("""\n
def network(x: np.ndarray) -> np.ndarray:
    """)
    for i in range(len(model)):
        layer = model[i]
        if isinstance(layer, nn.ReLU):
            # ignore. we cover these in the perceptron code.
            continue
        
        if debug_i != -1 and i == debug_i:
            break
        
        single_file.append(f"    x = l{i}_g(x)\n")
        continue

    single_file.append("    return x\n")
    single_file.append("""
import torch
def strvec(s):
    vec_in = torch.zeros(55)
    for i, c in enumerate(s):
        vec_in[i] = ord(c)
    vec_in = vec_in.to(torch.float32)
    return vec_in

y = network(strvec("password"))
print(y)
    """)
    open(f"analysis/layers2/single.py", "w").write('\n'.join(single_file))

dec_single_file(model)
# flush
