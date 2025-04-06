import torch
model = torch.load("js.pt", weights_only=False, map_location='cpu')

torch.no_grad()

# 7f 3b 5d 19 6e 2a 4c 08
# 127 59 93 25 110 42 76 8

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
# In the DES construction, the final output is a 64 byte block.
# This 64-bit block is the ciphertext.
# 
# So with that in mind, this network discretely approximates DES?
# It takes what looks like a key (55 bits)?
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

# Each DES key is 8 odd-parity bytes, with 56 bits of key and 8 bits of error-detection
# https://en.wikipedia.org/wiki/Triple_DES
# matches perfectly with the 55 feature in

# # Generated from reverse engineering
# def l6_g(x: np.ndarray) -> np.ndarray:
#     # x is a list (or vector) of length 208
#     out = np.empty(208, dtype=np.float32)



def hex_to_input(hex_str: str) -> torch.Tensor:
    # convert hex string to binary
    binary_str = bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)
    # >>> hex(int("1000000011000100101000101110011010010001110101011011001111110111",2))
    # '0x80c4a2e691d5b3f7'
    return torch.tensor([float(c) for c in binary_str])

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

# convert hex string to binary
# hex_str = "80c4a2e691d5b3f7" # constnat, also DES test vector key
hex_str = "70617373776f7264" # plaintext - "password"
# hex_str = "73fa80b66134e403" # ciphertext - enc("password")
# hex_str = "7f3b5d196e2a4c08" # other constant

input = hex_to_input(hex_str)

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