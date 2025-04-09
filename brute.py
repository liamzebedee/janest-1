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

def des_key_to_vector(key_hex: str) -> torch.Tensor:
    """
    Convert a 64-bit DES key (hex string of length 16) into a 56-element Torch tensor,
    dropping the least significant (parity) bit from each byte.
    
    For example, given key "80c4a2e691d5b3f7", we convert it to a 64-bit binary string,
    split it into 8 bytes, drop the last bit of each byte, and then output a tensor
    of 56 floats (0.0 or 1.0).
    """
    # Convert hex to 64-bit binary string (padded with zeros if necessary)
    key_int = int(key_hex, 16)
    bin_str = format(key_int, '064b')
    
    bits = []
    for i in range(8):
        byte = bin_str[i*8:(i+1)*8]  # Get 8 bits of the byte
        bits.extend(byte[:7])         # Drop the last bit (assumed parity)
    
    # Convert list of '0' and '1' to float values and create a torch tensor
    vector = torch.tensor([float(b) for b in bits], dtype=torch.float32)
    return vector

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
    # vec_in[0] = 255.0
    return vec_in

model = torch.load("js.pt", weights_only=False, map_location='cpu')
torch.set_num_threads(32)

# cut the model to the last layer
cut_model = True
cut_model = False
if cut_model:
    model_cut = torch.nn.Sequential(*list(model.children())[:-2])
    model = torch.nn.Sequential(model_cut)

y = model(strvec("b"))
print(f"cut_model: {cut_model}")
print(model[-1])
print(type(model[-1]))
print("output shape: ", y.shape)

# quantize.
# import torch.quantization as tq
# print("quantizing...")
# model.eval()
# model.qconfig = tq.default_qconfig
# model_fp32_prepared = tq.prepare(model)
# model = tq.convert(model_fp32_prepared)
# print("done")

# Pre-generate inputs to avoid generating them in the loop
# inputs = [strvec(f"80c4a2e691d5b3f7{i:02x}") for i in range(100)]


inputs = [
    strvec("password"),
    # des_key_to_vector("80c4a2e691d5b3f7"),
    # des_key_to_vector("7f3b5d196e2a4c08"),
    des_key_to_vector("73fa80b66134e403"),
    
    # hexvec("6bc1bee22e409f96e93d7e117393172a"),
    # strvec("T(d@U)eAV*fB"),
    # strvec("janest"),
    # strvec("admin"),
    # strvec("pass"),
]

# for x in ['7f3b5d1980c4a200', 'e67f3b5d19000000', '000091d5b3f78000', 'c4a2e67f3b5d1900', '80c4a2e600000000', '006e2a4c08000000']:
#     inputs.append(hexvec(x))


# Iterate over predefined inputs and test with the model
for x in inputs:
    print(f"Input vector: {x}")
    y = model(x)
    
    print("\033[92m", end="")  # Set output color to green
    print(f"Model output: {y}")
    print("\033[0m", end="")  # Reset output color
    # if model.shape == (1,)
    # if y == 1 or y == 1.0 or y == '1':
    #     print(f"Found solution: {input_str}")
    #     exit()
    
    # log the iterations per second
    # print(f"Iterations per second: {i / time.time()}")