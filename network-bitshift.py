# 
# A network to model the function: 
# y = x << y
# where x is an integer, y is a bit-shift amount.
# 
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import numpy as np

# device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
device = torch.device("cpu")
import os
torch.set_num_threads(os.cpu_count())


# Do some modelling on the minimum architecture of this network.
import math
def min_iterations(epsilon):
    b = 8
    ln2 = math.log(2)
    x = b * ln2  # This is 8*ln2
    n = 0
    # Check the (n+1)th term in the series expansion of e^(x)
    term = (x ** (n+1)) / math.factorial(n+1)
    while term >= epsilon:
        n += 1
        term = (x ** (n+1)) / math.factorial(n+1)
    return n

# Example: determine iterations for a tolerance of 1e-6
epsilon = 1e-8
min_iterations = min_iterations(epsilon)
print("Minimum iterations needed:", min_iterations)
# exit()


# Straight-Through Estimator for rounding (discrete quantization)
class STEQuantize(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        return torch.round(input)  # Discrete output

    @staticmethod
    def backward(ctx, grad_output):
        return grad_output  # Identity gradient

# Minimal network performing a bit shift (multiplication by 2)
class BitShiftNetwork(nn.Module):
    def __init__(self):
        super(BitShiftNetwork, self).__init__()
        # Model learns:
        # a << b = a * 2^b
        # f(x) = a * 2^b where x = [a, b]
        # f(x) = x_1 * 2^x_2

        # Setup architecture.
        self.layers = nn.ParameterList()
        inner_dim = 16
        self.layers.append(nn.Linear(2, inner_dim, bias=True))
        for i in range(min_iterations):
            self.layers.append(nn.Linear(inner_dim, inner_dim, bias=True))
            self.layers.append(nn.ReLU())
        self.layers.append(nn.Linear(inner_dim, 1, bias=True))


    def forward(self, x):
        y = x
        for layer in self.layers:
            y = layer(y)
        # Apply STE quantization to enforce discrete-like outputs
        return STEQuantize.apply(y)

def create_dataset():
    # Create data set (true distribution):
    # x : a,b
    # y : a << b
    NUM_SAMPLES = 500
    a_vals = np.random.randint(low=0, high=5, size=(NUM_SAMPLES))
    b_vals = np.random.randint(low=0, high=8, size=(NUM_SAMPLES))
    # compute y_vals
    # y = a << b
    print(a_vals)
    y_vals = np.zeros(len(a_vals))
    for i in range(len(y_vals)):
        # y = a << b
        y_vals[i] = a_vals[i] * (2 ** b_vals[i])
    print(y_vals)

    # Compute x,y
    x_vals = np.column_stack((a_vals[:], b_vals[:]))
    y_vals = y_vals[:]
    # save to file.
    np.savez('bitshift-data.npz', x=x_vals, y=y_vals)

# Load dataset
dataset = np.load('bitshift-data.npz')
x_data = dataset['x']
y_data = dataset['y']

# Split into training and validation sets:
# x_train, y_train
# x_val, y_val
# 80% training, 20% validation
split_idx = int(0.8 * len(x_data))
x_train = x_data[:split_idx]
y_train = y_data[:split_idx]
x_val = x_data[split_idx:]
y_val = y_data[split_idx:]
print(x_train[0:5], y_train[0:5])

# print lengths
print(len(x_train))
print(len(y_train))
print(len(x_val))
print(len(y_val))

y_train = y_train.reshape(-1, 1)  # Reshape y_train to have shape [num_samples, 1]
y_val = y_val.reshape(-1, 1)      # Reshape y_val to have shape [num_samples, 1]

train_dataset = TensorDataset(torch.tensor(x_train, dtype=torch.float32), torch.tensor(y_train, dtype=torch.float32))
val_dataset = TensorDataset(torch.tensor(x_val, dtype=torch.float32), torch.tensor(y_val, dtype=torch.float32))

print(train_dataset[0:5])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, pin_memory=True)
val_loader = DataLoader(val_dataset, batch_size=32, pin_memory=True )


# if device.type == "mps":
#     train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=0, pin_memory=False)
#     val_loader = DataLoader(val_dataset, batch_size=32, num_workers=0, pin_memory=False)


# Initialize network, loss, and optimizer
model = BitShiftNetwork().to(device)
# Load model weights if they exist.
if os.path.exists('bitshift-weights.pt'):
    model.load_state_dict(torch.load('bitshift-weights.pt'))
lossf = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=10)
# optimizer = optim.SGD(model.parameters(), lr=0.001)

# Training loop
# Train until validation loss is 0
epoch = 0
while True:
    import time

    # Training step
    model.train()
    train_loss = 0.0
    start_time = time.time()
    steps = 0
    for x_batch, y_batch in train_loader:
        optimizer.zero_grad()
        output = model(x_batch)
        loss = lossf(output, y_batch)
        loss.backward()
        optimizer.step()
        train_loss += loss.item() * x_batch.size(0)
        steps += 1

    train_loss /= len(train_dataset)
    train_time = time.time() - start_time

    # if train_loss < 100, save the model and training data.
    # if train_loss < 100:
    #     torch.save(model.state_dict(), 'bitshift-weights.pt')
    #     np.savez('bitshift-data.npz', x=x_train, y=y_train)
    #     break

    # Calculate steps per second
    steps_per_second = steps / train_time

    # Validation evaluation
    model.eval()
    val_loss = 0.0
    start_time = time.time()
    step = 0
    with torch.no_grad():
        for x_batch, y_batch in val_loader:
            output = model(x_batch)
            loss = lossf(output, y_batch)
            val_loss += loss.item() * x_batch.size(0)
            step += 1
            log_step = True
            if log_step:
                val_loss /= len(val_dataset)
                val_time = time.time() - start_time
                print(f"Epoch {epoch+1} completed. Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}, Steps per Second: {steps_per_second:.2f}, Train Time: {train_time:.2f}s, Val Time: {val_time:.2f}s")
    
    # Update the learning rate using the scheduler
    scheduler.step(train_loss)
    
    if val_loss == 0.0:
        break

    epoch += 1


# Test the network on the validation set
# net.eval()
# with torch.no_grad():
#     sample_out = net(x_val)
#     print("\nSample x:", x_val.squeeze().tolist())
#     print("Network Outputs:", sample_out.squeeze().tolist())
#     print("Expected Outputs:", (x_val * 2).squeeze().tolist())
