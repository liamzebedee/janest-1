import torch

def predict(text, model):
    with torch.no_grad():
        output = model(text)
        return float(output)

# If the entire model was saved:
model = torch.load("js.pt", weights_only=False, map_location='cpu')
# torch.load(model_path, weights_only=False, )
# model.eval()




# print_arch(model)

# Okay, how can we see what text causes activations? 
# Let's just start by running through a dictionary.

# for i in range(128):  # UTF-8 characters from 0 to 127
#     char = chr(i)
#     prediction = predict(char, model)
#     print(f"Character: {char}, Prediction: {prediction}")
# # All 0.

# Now try combinations of two words.
# import string

# alphanumeric_chars = string.ascii_letters + string.digits

# for char1 in alphanumeric_chars:
#     for char2 in alphanumeric_chars:
#         text = char1 + " " + char2
#         prediction = predict(text, model)
#         print(f"Character: {text}, Prediction: {prediction}")


# Now try constructing a noisey gaussian vector of the input size (55   )
# and see if the model can predict the output.

import torch
import numpy as np

# print like 50 of these different ones
# for i in range(50):
#     input_vector = torch.randn(55)
#     y = predict(input_vector, model)
#     if y != 0.0:
#         print(input_vector)
#         print(y)
#     else:
#         print("0")

torch.no_grad()

# setup one vector one-hot encoded
# vec = "hello"
# vec = torch.tensor([ord(c) for c in "hello"], dtype=torch.float32)

vec = torch.zeros(55)
# vec[0] = 0.5
# vec[0:10] = -0.5
# vec[10:20] = -0.5
# vec[20:30] = 0.5
# vec[30:40] = 0.5
# vec[40:50] = 0.5
# vec[50] = 0.5
# print(predict(vec, model))


# remove the last two layers of model
model = torch.nn.Sequential(*list(model.children())[:-2])
y = model(vec)
# run through all elements of y, check their floats have no decimal places ie. .0
for i in range(len(y)):
    if not isinstance(y[i], int):
        if y[i] % 1 != 0:
            print(f"Element {i} is not an integer: {y[i]}")

# convert y to string
y_str = int("".join(str(int(y[i])) for i in range(len(y))))
# print y as hex
print(y_str)
print(hex(y_str))


def test_hash_fn(text):
    vec_in = torch.zeros(55)
    for i, c in enumerate(text):
        vec_in[i] = ord(c)
    vec_in = vec_in.float()
    y = model(vec_in)
    # Sanity check: y should be a list of integers
    for i in range(len(y)):
        if not isinstance(y[i], int):
            if y[i] % 1 != 0:
                print(f"Element {i} is not an integer: {y[i]}")
    y_int = int("".join(str(int(y[i])) for i in range(len(y))))
    y_str = "".join(chr(int(y[i])) for i in range(len(y)))
    print(y_str)
    y_hex = hex(y_int)
    return y_hex

print(test_hash_fn("a" * 55))
print(test_hash_fn("world"))
print(test_hash_fn("hello world"))
print(test_hash_fn("world hello"))








# print(predict("1", model))

# Trick.
# - Two words
# - Look at last two layers
# - input: text, output: float
# Must be some sort of scoring NN? 

# Input: 55 float32
# Output: 1 float32

# Looks like a hash function:
# - pure feedforward, just linear + relu
# - phases: absorb, permute, squeeze/compress

