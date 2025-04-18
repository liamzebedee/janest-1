# Load js.pt
import torch
import numpy as np
from scipy.stats import entropy

js = torch.load('js.pt', weights_only=False)

def v1():
    # Print the value of weights for random 4 perceptrons for all the layers.
    for i in range(len(js)):
        # Print layer index and type
        print(f"Layer {i}: {type(js[i])}")
        # Skip if not Linear
        if type(js[i]) != torch.nn.Linear:
            continue
        
        # Get random 4 perceptrons.
        perceptrons = torch.randint(0, js[i].weight.shape[0], (4,))
        
        for p in perceptrons:
            print(f"  Perceptron {p}:")
            
            # weights
            weights = js[i].weight.data[p]
            # biases
            biases = js[i].bias.data[p]
            print(f"    Weights: {weights}")
            print(f"    Bias: {biases}")
        
        # Print the bias for the perceptrons.
        # for p in perceptrons:
        #     print(f"    Bias: {js[i].bias.data[p]}")


def v2():
    # Sample 1 input. ie. y = f(x).
    x = torch.randn(1, js[0].in_features)
    
    unique_weights = set()
    unique_biases = set()
    
    for i in range(min(100, len(js))):
        # Skip if not Linear
        if type(js[i]) != torch.nn.Linear:
            continue
        
        # Compute the output
        y = js[i](x)
        
        # Store unique values in weights and unique biases
        for p in range(js[i].weight.shape[0]):
            weights = js[i].weight.data[p].tolist()
            biases = js[i].bias.data[p].item()
            unique_weights.update(weights)  # Add unique values from the weights vector
            unique_biases.add(biases)
        
        # Update input for the next layer
        x = y
    
    # Print unique weights and biases
    print("Unique Weights:")
    for w in unique_weights:
        print(w)
    
    print("Unique Biases:")
    for b in unique_biases:
        print(b)



def v3(k=10):
    # Sample 1 input. ie. y = f(x).
    x = torch.randn(1, js[0].in_features)
    
    weight_entropies = []
    
    for i in range(len(js)):
        print(i)
        # Skip if not Linear
        if type(js[i]) != torch.nn.Linear:
            continue
        
        # Compute the output
        y = js[i](x)
        top_k_weights = []

        # Calculate entropy for each perceptron's weights
        for p in range(js[i].weight.shape[0]):
            weights = js[i].weight.data[p].numpy()
            weight_entropy = entropy(np.abs(weights))
            if len(top_k_weights) < k:
                top_k_weights.append((weight_entropy, weights))
            elif weight_entropy > top_k_weights[-1][0]:
                top_k_weights[-1] = (weight_entropy, weights)
                top_k_weights.sort(key=lambda x: x[0], reverse=True)
            
            # Prune the lowest entropy weight if more than k
            if len(top_k_weights) > k:
                top_k_weights.sort(key=lambda x: x[0], reverse=True)
                top_k_weights.pop()
        
        # Update input for the next layer
        x = y
    
    # Print top k highest entropy weights
    print(f"Top {k} highest entropy weights:")
    for idx, (ent, weights) in enumerate(top_k_weights):
        print(f"Rank {idx + 1}: Entropy = {ent}")
        print(f"Weights: {weights}")




def binarray_to_hex(arr):
    # Convert the array of 1.0/0.0 into a string of bits.
    bits = ''.join('1' if x else '0' for x in arr)
    # Convert the bit string to an integer.
    n = int(bits, 2)
    # Calculate the number of hex digits needed (each hex digit represents 4 bits).
    num_hex_digits = (len(arr) + 3) // 4
    # Format the integer into a zero-padded hex string.
    return format(n, '0{}x'.format(num_hex_digits))

model = js
def v4():
    # We are going to look for biases that represent "store data".
    # This happens when:
    # - bias array is one hot encoded (1's and 0's)
    # Decode bias array to hex
    # output single line
    
    for i in range(len(model)):
        # if i % 250 == 0:
        #     print(i)
        # if i== 100: 
        #     return
        if type(model[i]) != torch.nn.Linear:
            continue
        
        # use torch to check if bias array is one hot encoded
        biases = model[i].bias.data.numpy()
        
        is_empty_bias = torch.all(torch.tensor(biases) == 0.0)
        # if is_empty_bias:
        #     continue
        
        # check if biases contain only 0 and or 1's
        is_binary_coded = all(b in [0.0, 1.0] for b in biases)
        
        # if not is_binary_coded:
        #     continue

        hex_biases = binarray_to_hex(biases)
        padded_hex_biases = hex_biases.rjust(448 // 4, '0')
        dddd = f"0x{padded_hex_biases} (len={len(biases):3d}) (layer={i:5d})"
        
        print(dddd)
    

# v2()
# v3()
v4()