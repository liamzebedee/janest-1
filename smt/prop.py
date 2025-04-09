from os.path import realpath

with open("property.txt", "w") as f:
    for i in range(55):
        f.write(f"x{i} >= 0\n")
        f.write(f"x{i} <= 1\n")
    f.write("y0 >= 1\n")
    f.write("y0 <= 1\n")

# with open("property.txt", "w") as f:
#     for i in range(55):
#         f.write(f"input[{i}] >= 0\n")
#         f.write(f"input[{i}] <= 1\n")
#     f.write("output = 1\n")


# Define model dimensions
num_inputs = 55  # Number of input variables
num_outputs = 0  # Number of output variables
total_vars = num_inputs + num_outputs  # Total variables (inputs + outputs)


# Open file and write the input query
with open("input_query.txt", "w") as f:
    # Number of variables
    f.write(f"{total_vars}\n")

    # Number of lower bounds (one for each variable)
    lower_bounds = []
    for i in range(num_inputs):
        lower_bounds.append(f"{i},0.0\n")
    
    f.write(f"{len(lower_bounds)}\n")
    for lb in lower_bounds:
        f.write(lb)
    
    
    # num_lower_bounds = num_inputs
    # f.write(f"{num_lower_bounds}\n")
    # Lower bounds for inputs (0 to num_inputs-1)
    # for i in range(num_inputs):
    #     f.write()
    # Lower bound for output (index = num_inputs)
    # f.write(f"{num_inputs},1.0\n")
    
    # Number of upper bounds (one for each variable)
    upper_bounds = []
    for i in range(num_inputs):
        upper_bounds.append(f"{i},1.0\n")
    
    f.write(f"{len(upper_bounds)}\n")
    for lb in upper_bounds:
        f.write(lb)
    
    # Number of equations (none)
    f.write("0\n")
    
    # Number of nonlinear constraints (none)
    f.write("0\n")
    
    # Number of input variables
    f.write(f"{num_inputs}\n")
    # Input variable mappings (index,variable)
    for i in range(num_inputs):
        f.write(f"{i},{i}\n")
    
    # Number of output variables
    f.write(f"{num_outputs}\n")
    # Output variable mapping (index 0 maps to variable num_inputs)
    f.write(f"0,{num_inputs}\n")

# from os.path import realpath
# with open("input_query.txt", "w") as f:
#     f.write(f"Network: {realpath('js.onnxsim.onnx')}\n")
#     f.write("55\n")  # Input count
#     f.write(" ".join(str(i) for i in range(55)) + "\n")
#     f.write("1\n55\n")  # Output count and index
#     f.write("56\n")  # Total variables
#     f.write("56\n")  # Lower bound count
#     for i in range(55): f.write(f"{i},0.0\n")
#     f.write("55,1.0\n")
#     f.write("56\n")  # Upper bound count
#     for i in range(55): f.write(f"{i},1.0\n")
#     f.write("55,1.0\n")
#     f.write("0\n0\n")  # No equations or constraints