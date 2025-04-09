import torch
model = torch.load("js.pt", weights_only=False, map_location='cpu')

torch.no_grad()

# 7f 3b 5d 19 6e 2a 4c 08
# 127 59 93 25 110 42 76 8

# 7f3b5d196e2a4c08
# 80c4a2e691d5b3f7

# Okay what have we found from tonight?
# inside layer 6, there is a bias of 0x80c4a2e691d5b3f77f3b5d196e2a4c08
# def l6_g(x: np.ndarray) -> np.ndarray:
# Splitting this bias into 2, 80c4a2e691d5b3f7 and 7f3b5d196e2a4c08
# 1. The first half is the constant DES key. This is the key used to encrypt the plaintext "password"
# 2. The second half is ???
# 
# Reading up on the model as if it were a DES implementation, this makes sense.
# DES key size is 56 bits, our input is vector of 55.
# 
# Looking at the architecture:
# l0:
    # 1. Copies the first 55 bits range(0, 55)
    # 2. Pads with 1 bit 56
    # 3. Copies the first 55 bits range(56, 111)
    # 4. Copies the first 55 bits, all *-1 range(112, 167)
        # potential subtract?
        # sets all bits to 0 here
    # 5. Sets seq info -1 to 55 in range(167, 224)
# l2:   
    # 1. Copies the first 56 bits range(0, 56)
    # 2. Some crazy shit. LOoks like mad masking additions
        # x[56] = (x & add_mask >> 0) - (x & sub_mask)
        # x[57] = (x & add_mask >> 1) - (x & sub_mask)
        # x[58] = (x & add_mask >> 2) - (x & sub_mask)
    # 3. Sets to 0 range(225, 232)
# l4:
    # 1. Sets 0->56 bits to some combo of 
        # Looks like add and subtract of 4 56-bit parts based on some bitmask of prev layer
        # x[0:56] + -1 * x[56:112]<<7 + -1*x[112:168]<<8 + 1*x[168:224]<<7
        
        # s = x[0 + i] + 1*(x[i + 56] << 7) + -1*(x[i + 112] << 8) + 1*(x[i + 168] << 7)
        # out[0 + i] = s if s > 0 else 0.0 # ReLu
    # 2. Sets 56->64 to the 0 bits from 224->232
# l6:
    # Finally l6 is where we see this magic.
    # 1. we store magic DES key for range(0, 128) - 80c4a2e691d5b3f7 7f3b5d196e2a4c08
    # 2. store 4 bits x[0:4]  in range(128, 132)
    # 3. store 4 bits -x[0:4] in range(132, 136)
    # 4. store 4 bits x[0:4]-127 in range(136, 140)
    # 5. store 4 bits x[0:4]-128 in range(140, 144)
    # 6. store 64 bits of x in range(144, 208)
# ...
# l34:
    # This is where we first use the DES key.
    # 1. Store 128 bits of x in range(0, 128)
    # 2. 
        # out(128, 160) = x[0:32] + x[32:64] - 1
        # ..
        # s = x[32 + i] + x[64 + i]
    # ...
    # interesting constant: 0x1e2556eb
# ...
# l5438: (192 -> 48)
    # 1. Looks like a permutation. In terms of DES, this resembles the inverse of the initial permutation.
# l5441: Relu
# l5440: (48 -> 1)
    # 1. x = x[0:16] + x[32:48] - (x[16:32] << 1)
    # 2. x = x - 15 = x - (2**4 + 1) = (x << 4) - 1
# l5441: Relu
# 
# (5436): Linear(in_features=320, out_features=192, bias=True)
# (5437): ReLU()
# (5438): Linear(in_features=192, out_features=48, bias=True)
# (5439): ReLU()
# (5440): Linear(in_features=48, out_features=1, bias=True)
# (5441): ReLU()
# 
# The final outputs of our NN are the 48 outputs of the last ReLU.
# In the DES construction, the final output is a 64 bit block.
# This 64-bit block is the ciphertext.
# 
# So with that in mind, this network discretely approximates DES?
# It takes what looks like a key (55 bits)?
# 
# Time to break it down:
# H1: this is a DES cipher.
    # What evidence do we have?
    # 1. There's a DES key in here
    # 2. It has permutations and mixing and potentially S tables
    # 3. It takes a 55 bit key
# H2: the embedded constant
    # 1. it's a lookup table
    # 2. it's a key 
# H3: the input is 55 bits.
    # E1: the l0 does binary logic on the input (-1). this implies the input is 55 bits.
# Observations:
    # O1: The output is a 0 or 1 bit. This indicates some predicate.
        # a. input=key, output=did_decrypt?
    # O2: The constant - idk what it does yet.
    # O3: the l0 does binary logic on the input (-1). plus a padding bit. this implies the input is 55 bits.
    # O4: the ouput of the 48 layer is bytes (i e [0,256]). 48 bytes of output.
# Questions:
    # Q1: what does the network do?
        # input is key, f is ???, output is 0 or 1 (success/failure)
        # input is key, f is ???, output is 48 bytes = 384 bits
        # it could still be a hash function.
# 2. H: input is key?
# 3. H: input is plaintext?
# 4. H: input is ciphertext?
# 
# 
# 
# 

# https://en.wikipedia.org/wiki/DES_supplementary_material

# https://www.cse.iitb.ac.in/~puru/courses/resources/old-virtio/qemu/tests/unit/test-crypto-cipher.c
# https://www.cse.iitb.ac.in/~puru/courses/resources/old-virtio/qemu/tests/unit/test-crypto-cipher.c
# {
#     /*
#      * Testing 'password' as plaintext fits
#      * in single AES block, and gives identical
#      * ciphertext in ECB and CBC modes
#      */
#     .path = "/crypto/cipher/des-ecb-56-one-block",
#     .alg = QCRYPTO_CIPHER_ALGO_DES,
#     .mode = QCRYPTO_CIPHER_MODE_ECB,
#     .key = "80c4a2e691d5b3f7",
#     .plaintext = "70617373776f7264",
#     .ciphertext = "73fa80b66134e403",
# },
# {
#     /* See previous comment */
#     .path = "/crypto/cipher/des-cbc-56-one-block",
#     .alg = QCRYPTO_CIPHER_ALGO_DES,
#     .mode = QCRYPTO_CIPHER_MODE_CBC,
#     .key = "80c4a2e691d5b3f7",
#     .iv = "0000000000000000",
#     .plaintext = "70617373776f7264",
#     .ciphertext = "73fa80b66134e403",
# },
# {
#     .path = "/crypto/cipher/des-ecb-56",
#     .alg = QCRYPTO_CIPHER_ALGO_DES,
#     .mode = QCRYPTO_CIPHER_MODE_ECB,
#     .key = "80c4a2e691d5b3f7",
#     .plaintext =
#         "6bc1bee22e409f96e93d7e117393172a"
#         "ae2d8a571e03ac9c9eb76fac45af8e51"
#         "30c81c46a35ce411e5fbc1191a0a52ef"
#         "f69f2445df4f9b17ad2b417be66c3710",
#     .ciphertext =
#         "8f346aaf64eaf24040720d80648c52e7"
#         "aefc616be53ab1a3d301e69d91e01838"
#         "ffd29f1bb5596ad94ea2d8e6196b7f09"
#         "30d8ed0bf2773af36dd82a6280c20926",
# },
# plaintext = 6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411e5fbc1191a0a52eff69f2445df4f9b17ad2b417be66c3710
# ciphertext = 8f346aaf64eaf24040720d80648c52e7aefc616be53ab1a3d301e69d91e01838ffd29f1bb5596ad94ea2d8e6196b7f0930d8ed0bf2773af36dd82a6280c20926

# 2d00882d45000000280d15005c0000002e00892e46000000290e16005d0000002f008a2f470000002a0f17005e000000

# Each DES key is 8 odd-parity bytes, with 56 bits of key and 8 bits of error-detection
# https://en.wikipedia.org/wiki/Triple_DES
# matches perfectly with the 55 feature in

# # Generated from reverse engineering
# def l6_g(x: np.ndarray) -> np.ndarray:
#     # x is a list (or vector) of length 208
#     out = np.empty(208, dtype=np.float32)




# output shape:  torch.Size([48])
# Model output: tensor([  0.,   0., 148.,   0.,   0.,   0.,   0.,  22.,   0.,  56.,  10.,   0.,
#           0.,   0.,   0., 100.,   0.,   0., 149.,   0.,   0.,   0.,   0.,  23.,
#           0.,  57.,  11.,   0.,   0.,   0.,   0., 101.,   0.,   0., 150.,   0.,
#           0.,   0.,   0.,  24.,   0.,  58.,  12.,   0.,   0.,   0.,   0., 102.],
#        grad_fn=<ReluBackward0>)
# Model output: tensor([  0.,   0.,   0., 120.,   0.,   0.,   0., 109.,   0.,  63.,   0.,   0.,
#           0.,   0.,   0.,   0.,   0.,   0.,   0., 121.,   0.,   0.,   0., 110.,
#           1.,  64.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0., 122.,
#           0.,   0.,   0., 111.,   2.,  65.,   0.,   0.,   0.,   0.,   0.,   0.],
#        grad_fn=<ReluBackward0>)
# Model output: tensor([  0.,   0., 129.,  56.,   0.,   0.,   0., 178.,   0.,   0.,   0.,   0.,
#          22.,  28.,   0.,  24.,   0.,   0., 130.,  57.,   0.,   0.,   0., 179.,
#           0.,   0.,   0.,   0.,  23.,  29.,   0.,  25.,   0.,   0., 131.,  58.,
#           1.,   0.,   0., 180.,   0.,   0.,   0.,   0.,  24.,  30.,   0.,  26.],
#        grad_fn=<ReluBackward0>)
# Model output: tensor([  0.,   0.,   1.,   3.,  66.,  94.,   0., 180.,   0.,   0.,  48.,  27.,
#          21.,  75.,   0.,   0.,   0.,   0.,   2.,   4.,  67.,  95.,   0., 181.,
#           0.,   0.,  49.,  28.,  22.,  76.,   0.,   0.,   0.,   0.,   3.,   5.,
#          68.,  96.,   0., 182.,   0.,   0.,  50.,  29.,  23.,  77.,   0.,   0.],
#        grad_fn=<ReluBackward0>)
# Model output: tensor([  0.,   0.,   0.,   0.,  59.,   0.,   0., 194.,   0.,   0.,   0.,   0.,
#          15.,   0.,   0.,  78.,   0.,   0.,   0.,   0.,  60.,   0.,   0., 195.,
#           0.,   0.,   0.,   0.,  16.,   0.,   0.,  79.,   0.,   0.,   0.,   0.,
#          61.,   0.,   0., 196.,   0.,   0.,   0.,   0.,  17.,   0.,   0.,  80.],
#        grad_fn=<ReluBackward0>)
# Model output: tensor([  0.,   0.,  16.,   1., 134.,  51.,   0.,   3.,   0.,   0.,   0.,   0.,
#           0.,  70.,   0.,   3.,   0.,   0.,  17.,   2., 135.,  52.,   0.,   4.,
#           0.,   0.,   0.,   0.,   0.,  71.,   0.,   4.,   0.,   0.,  18.,   3.,
#         136.,  53.,   0.,   5.,   0.,   0.,   0.,   0.,   0.,  72.,   0.,   5.],
#        grad_fn=<ReluBackward0>)
# Model output: tensor([  0.,   0.,   0.,  13.,   0., 185.,   0.,  66.,   0.,   3.,   0.,   5.,
#         107.,   0.,   0., 117.,   0.,   0.,   0.,  14.,   0., 186.,   0.,  67.,
#           0.,   4.,   0.,   6., 108.,   0.,   0., 118.,   0.,   0.,   0.,  15.,
#           0., 187.,   0.,  68.,   0.,   5.,   0.,   7., 109.,   0.,   0., 119.],
#        grad_fn=<ReluBackward0>)
# Model output: tensor([  0.,   0., 148.,   0.,   0.,   0.,   0.,  22.,   0.,  56.,  10.,   0.,
#           0.,   0.,   0., 100.,   0.,   0., 149.,   0.,   0.,   0.,   0.,  23.,
#           0.,  57.,  11.,   0.,   0.,   0.,   0., 101.,   0.,   0., 150.,   0.,
#           0.,   0.,   0.,  24.,   0.,  58.,  12.,   0.,   0.,   0.,   0., 102.],




# Generated from reverse engineering
def l5410_g(x: np.ndarray) -> np.ndarray:
    # x is a list (or vector) of length 320
    out = np.empty(320, dtype=np.float32)
    
    biases = [0.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, -1.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, -1.0]
    # for i in range(0, 32):
    for i in range(0, 32):
        s = x[0 + i]
        s += biases[i]
        out[0 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x80c4a2e6 (len=32)
    biases = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0]
    # for i in range(32, 64):
    for i in range(0, 32):
        s = x[0 + i]
        s += biases[i]
        out[32 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [0.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 0.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, -1.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, -1.0]
    # for i in range(64, 96):
    for i in range(0, 32):
        s = x[0 + i]
        s += biases[i]
        out[64 + i] = s if s > 0 else 0.0 # ReLu
        
    # for i in range(96, 128):
    for i in range(0, 32):
        s = x[32 + i] + -1 * -2.0 * x[i + 64]
        out[96 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x91d5b3f7 (len=32)
    biases = [1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0]
    # for i in range(128, 160):
    for i in range(0, 32):
        s = 0
        s += biases[i]
        out[128 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, -1.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0, 0.0, -1.0, -1.0, 0.0]
    # for i in range(160, 192):
    for i in range(0, 32):
        s = x[96 + i]
        s += biases[i]
        out[160 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x7f3b5d19 (len=32)
    biases = [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0]
    # for i in range(192, 224):
    for i in range(0, 32):
        s = x[96 + i]
        s += biases[i]
        out[192 + i] = s if s > 0 else 0.0 # ReLu
        
    biases = [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, -1.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0, 0.0, -1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    # for i in range(224, 288):
    for i in range(0, 64):
        s = x[96 + i]
        s += biases[i]
        out[224 + i] = s if s > 0 else 0.0 # ReLu
        
    # biases: 0x6e2a4c08 (len=32)
    biases = [0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
    # for i in range(288, 320):
    for i in range(0, 32):
        s = 0
        s += biases[i]
        out[288 + i] = s if s > 0 else 0.0 # ReLu
        
    return out






def hex_to_input(hex_str: str) -> torch.Tensor:
    # convert hex string to binary
    binary_str = bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)
    # >>> hex(int("1000000011000100101000101110011010010001110101011011001111110111",2))
    # '0x80c4a2e691d5b3f7'
    return torch.tensor([float(c) for c in binary_str])


# [ 45.   0. 136.  45.  69.   0.   0.   0.  40.  13.  21.   0.  92.   0.
#    0.   0.  46.   0. 137.  46.  70.   0.   0.   0.  41.  14.  22.   0.
#   93.   0.   0.   0.  47.   0. 138.  47.  71.   0.   0.   0.  42.  15.
#   23.   0.  94.   0.   0.   0.]

def tensor_u256_to_hex(tensor: torch.Tensor) -> str:
    return tensor.astype(np.uint8).tobytes().hex()

def tensor_to_bin_to_hex(tensor: torch.Tensor) -> str:
    # convert tensor to binary string
    bin_str = "".join(str(int(tensor[i])) for i in range(len(tensor)))
    # convert binary string to hex string
    return hex(int(bin_str, 2))[2:]

def tensor_to_hex(tensor: torch.Tensor) -> str:
    # convert tensor to hex string
    # each item is a byte
    return "".join(f"{int(tensor[i]):02x}" for i in range(len(tensor)))

def hex_to_string(hex_str: str) -> str:
    # convert hex string to string
    return bytes.fromhex(hex_str).decode('utf-8')

import torch
def strvec(s):
    vec_in = torch.zeros(55)
    for i, c in enumerate(s):
        vec_in[i] = ord(c)
    vec_in = vec_in.to(torch.float32)
    return vec_in

# convert hex string to binary
hex_str = "80c4a2e691d5b3f7" # constnat, also DES test vector key
# hex_str = "70617373776f7264" # plaintext - "password"
# hex_str = "73fa80b66134e403" # ciphertext - enc("password")
# hex_str = "7f3b5d196e2a4c08" # other constant
input = strvec(hex_str)
# input = hex_to_input(hex_str)

# run the model
output = float(model(input))
print("output: "+str(output))

# 
LAYER_320 = 5434 # 320 outputs: range -1-2 (4 vals)
LAYER_192 = 5436 # 192 outputs: range -1-2 (4 vals)
LAYER_48 = 5438 # 48 outputs: range -256-256 (512 vals)
selected_layer = LAYER_48

model_cut = torch.nn.Sequential(*list(model.children())[:selected_layer + 2])
print(model_cut[-1])
model = torch.nn.Sequential(model_cut)
y = model(input[0:55])
print(y.shape)

print(f"y: {y}")

import sys
for v in y:
    c = int(v.item())
    # sys.stdout.write(chr(int(v.item())))
    # write hex char
    sys.stdout.write(f"{int(v.item()):02x}")
print()

# if selected_layer == LAYER_48:
#     # the output tensor each element is in range [-255, 255]
#     # interpret each digit as a base-512 digit
#     # and then convert to hex
#     def tensor_to_base512_hex(tensor: torch.Tensor) -> str:
#         base512_str = ""
#         for i in range(len(tensor)):
#             value = int(tensor[i].item())
#             if value < 0:
#                 value += 512
#             base512_str += f"{value:03x}"
#         return base512_str

#     y_base512_hex = tensor_to_base512_hex(y)
#     print(f"y(base512_hex): {y_base512_hex}")

# print(y)
print(f"y(bin2hex): {tensor_to_bin_to_hex(y)}")
print(f"y(bin2hex2utf): {hex_to_string(tensor_to_bin_to_hex(y))}")
print(f"y(hex): {tensor_to_hex(y)}")
try:
    print("y(str): "+hex_to_string(tensor_to_hex(y)))
except Exception as e:
    print(f"ex: {e}")

# convert y to binary
# y_bin = "".join(str(int(y[i])) for i in range(len(y)))
# print(y_bin)