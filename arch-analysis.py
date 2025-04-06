import torch

# If the entire model was saved:
model = torch.load("js.pt", weights_only=False, map_location='cpu')

# Print for each layer, every number of outputs
def print_arch(model):
    import sys
    torch.no_grad()

    # 1. Construct sequence.
    # Each Linear layer has an in and out dimension.
    # We skip ReLu activations.
    # We only need to log the first input and the output of each linear layer.
    # Since matrix multiplication is distributive, we don't care about the input size.
    seq = []
    for i, layer in enumerate(model):
        if not hasattr(layer, "in_features"):
            continue # Skip ReLu's
        # Only log the first input.
        if len(seq) == 0:
            pass
            seq.append(layer.in_features)
        # Only log output layer features.
        seq.append(layer.out_features)
    
    # 2. Identify unique dimensions.
    unique_dims = set(seq)
    print(f"Sequence length: {len(seq)}")
    print(f"Unique dimensions (n={len(unique_dims)}): {unique_dims}")

    # 3. Identify the number of layers with each unique dimension.
    layer_counts = {}
    for dim in unique_dims:
        layer_counts[dim] = seq.count(dim)
    print("Layer sizes:")
    layer_counts_sorted = sorted(layer_counts.items(), key=lambda item: item[1])
    for dim, count in layer_counts_sorted:
        print(f"{dim}: {count}")

    # 4. Print the sequence.
    print(f"Sequence:")
    print(seq)

    # 5. Output seq to seq.txt
    with open("seq.txt", "w") as f:
        f.write(",".join(map(str, seq)))

    sys.exit(0)

def print_inferred_arch():
    comp = ['55', '224', '232', '64', '208', '200', '212', '204', '216', '208', '220', '212', '224', '216', '228', '220', '232', '224', 'F', 'F', 'F', 'F', 'G', 'G', 'G', 'G', 'D', 'D', 'D', 'D', 'D', '256', '256', '256', '256', '287', '319', '318', '318', '316', '316', '312', '312', '304', '304', '256', '192', 'E', 'E', '320', '320', '382', '446', '444', '444', '440', '440', '432', '432', '416', '416', '320', '192', '48', '1']

    grammar = {'A': ['340', '332', '375', '399', '410', '402', '412', '404', '412', '404', '408', '400', '352', '288', '288', '256', '319', '288', '318', '288', '316', '288', '312', '288', '304', '288', '256', '288', '256', '319', '288', '318', '288', '316', '288', '312', '288', '304', '288', '256'], 'B': ['336', '296', 'A', '336', '296', 'A', '336', '296', 'A', '336', '296', 'A'], 'C': ['368', '328', 'A', '368', '328', 'A'], 'D': ['336', '328', 'A', '336', '328', 'A', '336', '328', 'A'], 'E': ['192', '160', '223', '192', '222', '192', '220', '192', '216', '192', '208', '192', '160'], 'F': ['B', 'B'], 'G': ['C', 'C']}

    def expand_sequence(compressed_seq, grammar):
        def expand_symbol(symbol):
            if symbol in grammar:
                expanded = []
                for item in grammar[symbol]:
                    expanded.extend(expand_symbol(item))
                return expanded
            else:
                return [symbol]

        expanded_seq = []
        for item in compressed_seq:
            expanded_seq.extend(expand_symbol(item))
        return expanded_seq

    # Example usage
    expanded_seq = expand_sequence(comp, grammar)
    print("Expanded sequence:")
    print(expanded_seq)

    # Convert the expanded sequence to a list of integers
    expanded_seq_int = list(map(int, expanded_seq))
    
    # Read the original sequence from seq.txt
    with open("seq.txt", "r") as f:
        original_seq = list(map(int, f.read().split(',')))

    # Check if the expanded sequence is equal to the original sequence
    if expanded_seq_int == original_seq:
        print("The expanded sequence matches the original sequence from seq.txt.")
    else:
        print("The expanded sequence does NOT match the original sequence from seq.txt.")

print_arch(model)
# print_inferred_arch()