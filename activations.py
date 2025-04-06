# Load js.pt
import torch

js = torch.load('js.pt')

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
