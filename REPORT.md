Jane Street Puzzle
==================

 - the neural network is a compilation of a digital circuit into Wx+b linear units and ReLu activations.
 - patterns used:
   - **Bit-parallel neuron**. Each neuron is a single bit. The neuron operates on multiple bits in parallel from the input (the previous layer's set of neurons - a bitstring).


## 3-DES.

 - 5442 layers
 - 2721 linear layers
 - Periodic spikes in your output-size graph → round structure
 - The model likely:
   - 3-DES.
   - DES has 16 rounds.
   - 3-DES has 48 rounds, following encrypt-decrypt-encrypt.
   - 2721/56 ~= 48.6.
 - Estimations.
   - 56 layers per DES round. 56*48 = 2688 layers.
   - Looking at arch graph (.ipynb), peaks end at 2632. Follows.
   - 2721-2688 = 33 layers remaining.
   - Final part of network resembles binary classifier.


## SMT solver.

It looks like at layer 18 we enter the 3DES cipher.
And 2678 or 2706 we exit it.

2706-18 = 2688
2778-18 = 2760

Plugging into our estimate for 1 DES iteration.
48 rounds.
2760/48=57.5
2778/48=57.8

I feel like
5410
Could be a good starting point
For where the binary comparator stuff happens
ie. where we exit DES, and begin the "special case check"

Let's slice the network here:
- slice the network
- generate python torch code
- insert the state dict
- convert to onnx
- simplify onnx
- generate property.txt 
- run marabou on it