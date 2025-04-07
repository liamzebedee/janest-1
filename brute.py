# gday bruce

import torch

def strvec(s):
    # convert s to binary ascii encoded of 1's and 0's
    s_bin = ''.join(bin(ord(c))[2:].zfill(8) for c in s)
    # print(s_bin, len(s_bin))
    vec_in = torch.zeros(55, dtype=torch.float32)
    for i, c in enumerate(s):
        vec_in[i] = float(s_bin[i])
    # print(vec_in)
    return vec_in

def hexvec(s):
    # check s is only hex chars
    if not all(c in '0123456789abcdef' for c in s):
        raise ValueError("Input string must contain only hex characters")
    # convert hex string to binary string
    s_bin = ''.join(bin(int(c, 16))[2:].zfill(4) for c in s)
    # print(s_bin, len(s_bin))
    vec_in = torch.zeros(55, dtype=torch.float32)
    for i, c in enumerate(s):
        vec_in[i] = float(s_bin[i])
    # print(vec_in)
    vec_in[0] = 255.0
    return vec_in

model = torch.load("js.pt", weights_only=False, map_location='cpu')
torch.set_num_threads(32)

# cut the model to the last layer
model_cut = torch.nn.Sequential(*list(model.children())[:-2])
model = torch.nn.Sequential(model_cut)
y = model(strvec("b"))
print(model_cut[-1])
print(type(model_cut[-1]))
print("output shape: ", y.shape)

# quantize.
import torch.quantization as tq
print("quantizing...")
model.eval()
model.qconfig = tq.default_qconfig
model_fp32_prepared = tq.prepare(model)
model = tq.convert(model_fp32_prepared)
print("done")

# Pre-generate inputs to avoid generating them in the loop
# inputs = [strvec(f"80c4a2e691d5b3f7{i:02x}") for i in range(100)]


inputs = [
    strvec("passwor"),
    hexvec("80c4a2e691d5b3f7"),
    hexvec("7f3b5d196e2a4c08"),
    hexvec("6bc1bee22e409f96e93d7e117393172a"),
    strvec("T(d@U)eAV*fB"),
    strvec("janest"),
    strvec("admin"),
    strvec("pass"),
]


# Iterate over predefined inputs and test with the model
for x in inputs:
    # print(f"Input vector: {x}")
    y = model(x)
    print(f"Model output: {y}")
    
    # if model.shape == (1,)
    # if y == 1 or y == 1.0 or y == '1':
    #     print(f"Found solution: {input_str}")
    #     exit()
    
    # log the iterations per second
    # print(f"Iterations per second: {i / time.time()}")