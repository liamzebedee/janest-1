import torch

# load model
model = torch.load("js.pt", weights_only=False, map_location='cpu')

# output to analysis/full-model-code.py
output_file = open("analysis/full-model-code.py", "w")
code_lines = []

# layer 0
