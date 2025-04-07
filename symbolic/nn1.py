import numpy as np

def relu(x):
    return np.maximum(0, x)



# Layer 1: Bit-Shift (t >> 24)
def layer_shift(t):
    # t: 32-bit binary vector, index 31 is MSB.
    # Output: extract bits 24–31 into an 8-bit vector.
    W_shift = np.zeros((8, 32))
    for i in range(8):
        W_shift[i, i + 24] = 1  # select t[i+24]
    b_shift = np.zeros(8)
    return relu(np.dot(W_shift, t) + b_shift)

# Layer 2: Bit-Mask (& 0x3F)
def layer_mask(y_shift):
    # y_shift: 8-bit vector; select lower 6 bits (indices 2 to 7)
    W_mask = np.zeros((6, 8))
    for i in range(6):
        W_mask[i, i + 2] = 1
    b_mask = np.zeros(6)
    return relu(np.dot(W_mask, y_shift) + b_mask)

# Utility: Convert 6-bit binary vector to one-hot vector (length 64)
def binary_to_one_hot(bits):
    index = 0
    for bit in bits:
        index = (index << 1) | int(bit)
    one_hot = np.zeros(64)
    one_hot[index] = 1
    return one_hot

# Layer 3: Array Lookup (sp2[...])
def layer_lookup(one_hot, sp2):
    # one_hot: 64-dim one-hot vector; sp2: list/array of 64 constants.
    W_lookup = np.array(sp2).reshape(1, 64)
    b_lookup = 0.0
    return np.dot(W_lookup, one_hot) + b_lookup

# Layer 4: XOR Operation using the provided gate table
def layer_xor(l, y_lookup):
    # l: original bit (scalar 0 or 1)
    # y_lookup: result from sp2 lookup (scalar)
    # XOR gate: output = ReLU(-l - y_lookup + 1)
    return relu(-l - y_lookup + 1)

# Assemble the network that mimics: l ^= sp2[(t >> 24) & 0x3F]
def layer_out(t, l, sp2):
    y_shift = layer_shift(t)     # Extract bits 24–31
    z = layer_mask(y_shift)      # Mask to lower 6 bits
    one_hot = binary_to_one_hot(z)  # Convert binary index to one-hot encoding (length 64)
    y_lookup = layer_lookup(one_hot, sp2)  # Lookup sp2 element
    return layer_xor(l, y_lookup)           # Compute XOR with l

# TODO;
sp2 = np.random.randint(0, 2, 64).astype(np.int32)

def ground_truth(t, l, sp2):
    # l ^= sp2[(t >> 24) & 0x3F];
    # convert inputs to py ints.
    # print(t,l)
    v = l ^ sp2[(t >> 24) & 0x3F]
    print(v)
    return v



def get_lookup_weights_and_biases():
    weights = []
    biases = []
    for i in range(64):
        row = []
        
        n = 6 # num bits
        for j in range(n):
            bit = (i >> (5 - j)) & 1  # extract bit (MSB first)
            w = 2.0 * bit - 1.0       # weight = 2*bit - 1 (i.e. +1 if bit==1, -1 if bit==0)
            row.append(w)
        weights.append(row)
        biases.append(n - 0.5)  # bias = n bits - 0.5
    return weights, biases

print(get_lookup_weights_and_biases()[0])
print(get_lookup_weights_and_biases()[1])
exit()

# Create 25 datums, split 80:20 train:test
data = np.random.randint(0, 2, (25, 32)).astype(np.int32)
labels = np.random.randint(0, 2, 25).astype(np.int32)

# Populate labels with ground truth.
for i in range(len(labels)):
    labels[i] = ground_truth(data[i], labels[i], sp2)

# Now evaluate the network on the dataset.
for i in range(len(data)):
    
    ypred = layer_out(data[i], labels[i], sp2)
    ytruth = labels[i]
    print(f"{ytruth} == {ypred}")
    
