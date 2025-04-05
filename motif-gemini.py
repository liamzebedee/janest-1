# By scanning the sequence of output dimensions, the overall structure appears to be:
# IB -> [A -> B -> C] * 7 -> [A' -> B -> C] * 5 -> [A'' -> B -> C] * 5 -> FB

# 18 + ((19 + 14 + 12) * 7) + ((19 + 14 + 12) * 5) + ((19 + 14 + 12) * 5) + 60

# In summary, the architecture starts with a unique block (IB), then enters a highly repetitive phase consisting of 17 repetitions of a three-block motif (A variant -> B -> C), and finally concludes with another unique block (FB) that reduces the dimension down to 1. There are 7 fundamental sequential patterns observed, with blocks B and C being the most frequently repeated individual sequences.

import torch
import torch.nn as nn
from typing import List

# --- Helper Function to Create a Block ---
def _create_block(block_dims: List[int]) -> nn.Sequential:
    """
    Creates a sequential block of Linear -> ReLU layers.

    Args:
        block_dims: A list of dimensions [in_dim, hidden1, hidden2, ..., out_dim].

    Returns:
        An nn.Sequential module representing the block.
    """
    layers = []
    if not block_dims or len(block_dims) < 2:
        # Return an empty sequential if dims are invalid/too short
        return nn.Sequential()

    for i in range(len(block_dims) - 1):
        in_dim = block_dims[i]
        out_dim = block_dims[i+1]
        layers.append(nn.Linear(in_dim, out_dim))
        # Add ReLU activation after every linear layer in the block
        layers.append(nn.ReLU())
    # The sequential block itself doesn't include the final non-linearity
    # if it's meant to be part of the final output layer of the whole network.
    # However, for internal blocks, ReLU is standard after each linear transform.
    return layers

# --- Define Dimensions for Each Identified Block Type ---
# These lists represent [block_input_dim, layer1_out, layer2_out, ..., block_output_dim]

# Note: These dimensions need to be extracted precisely from the full sequence.
# The example dimensions below are based on the previous analysis.

#IB:Input55,Output224(17layerswithinblock)
ib_dims=[55,224,232,64,208,200,212,204,216,208,220,212,224,216,228,220,232,224]

#A:Input224,Output256(18layerswithinblock)
a_dims=[224,336,296,340,332,375,399,410,402,412,404,412,404,408,400,352,288,288,256]

#B:Input256,Output256(13layerswithinblock)
b_dims=[256,319,288,318,288,316,288,312,288,304,288,256,288,256]

#C:Input256,Output256(11layerswithinblock)
c_dims=[256,319,288,318,288,316,288,312,288,304,288,256]

#A':Input256,Output256(18layerswithinblock)
a_prime_dims=[256,368,328,340,332,375,399,410,402,412,404,412,404,408,400,352,288,288,256]

#A'':Input256,Output256(18layerswithinblock)
a_prime_prime_dims=[256,336,328,340,332,375,399,410,402,412,404,412,404,408,400,352,288,288,256]

#FB:Input256,Output48(58layerswithinblock)-Sequenceneedscarefulextraction
#Examplestart/endbasedonanalysis-actuallistwouldbe~59elementslong
fb_dims=[256,256,256,256,256,287,319,318,318,316,316,312,312,304,304,256,192,192,160,223,192,222,192,220,192,216,192,208,192,160,160,192,160,223,192,222,192,220,192,216,192,208,192,160,160,320,320,382,446,444,444,440,440,432,432,416,416,320,192,48]


# --- Main Network Definition ---
class ComplexMLPFunctional(nn.Module):
    def __init__(self, final_output_dim=1):
        super().__init__()

        # --- Instantiate unique block types ---
        self.ib_block = _create_block(ib_dims)
        self.a_block = _create_block(a_dims)
        self.b_block = _create_block(b_dims)
        self.c_block = _create_block(c_dims)
        self.a_prime_block = _create_block(a_prime_dims)
        self.a_prime_prime_block = _create_block(a_prime_prime_dims)
        self.fb_block = _create_block(fb_dims)

        # --- Final output layer (no ReLU) ---
        # FB block outputs 48 features
        self.final_layer = nn.Linear(fb_dims[-1], final_output_dim)

        
    def forward(self, x):
        # Ensure input is batch_size x 55
        if x.ndim == 1:
            x = x.unsqueeze(0) # Add batch dimension if needed
        if x.shape[1] != ib_dims[0]:
             raise ValueError(f"Input vector size must be {ib_dims[0]}, but got {x.shape[1]}")

        # --- Execute the blocks sequentially ---
        # This forward pass explicitly defines the assumed block order.
        # THE EXACT SEQUENCE AND REPETITIONS BELOW NEED VERIFICATION AGAINST THE FULL LIST.

        x = self.ib_block(x) # Out: 224 features

        # First instance of A->B->C (A takes 224 input)
        x = self.a_block(x)  # Out: 256 features
        x = self.b_block(x)  # Out: 256 features
        x = self.c_block(x)  # Out: 256 features

        # Now repetitions involving A'' (takes 256 input) and A' (takes 256 input)
        # Example: Assuming 6 repetitions of A''->B->C
        for _ in range(6):
            x = self.a_prime_prime_block(x) # Out: 256
            x = self.b_block(x)             # Out: 256
            x = self.c_block(x)             # Out: 256

        # Example: Assuming 5 repetitions of A'->B->C
        for _ in range(5):
            x = self.a_prime_block(x)       # Out: 256
            x = self.b_block(x)             # Out: 256
            x = self.c_block(x)             # Out: 256

        # Example: Assuming 5 more repetitions of A''->B->C
        for _ in range(5):
            x = self.a_prime_prime_block(x) # Out: 256
            x = self.b_block(x)             # Out: 256
            x = self.c_block(x)             # Out: 256

        # Final Blocks
        x = self.fb_block(x) # Out: 48 features (fb_dims[-1])
        x = self.final_layer(x) # Out: final_output_dim (e.g., 1)

        return x

# --- Example Usage ---
# Instantiate the model
model = ComplexMLPFunctional(final_output_dim=1)

# Print the structure (shows the main components, not the full sequential expansion)
# print(model)

# Create a dummy input tensor (batch of 1, 55 features)
try:
    dummy_input = torch.randn(1, 55)
    # Perform a forward pass
    output = model(dummy_input)
    print(f"Input shape: {dummy_input.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Output value: {output.item()}")
except ImportError:
    print("PyTorch not found. Skipping model execution example.")
    print("Install PyTorch via https://pytorch.org/")
except Exception as e:
    print(f"An error occurred during model execution: {e}")
    print("This might be due to inaccuracies in block dimension definitions or the assumed forward pass sequence.")