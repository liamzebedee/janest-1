Dwarkesh Jane St problem
========================

Jane St problem from Dwarkesh podcast: https://x.com/dwarkesh_sp/status/1907886365565501568

 http://jane-st.co/dwarkesh-puzzle

## Problem.

Today I went on a hike and found a pile of tensors hidden underneath a neolithic burial mound!
        
I sent it over to the local neural plumber, and they managed to cobble together this.

**[model.pt](https://huggingface.co/jane-street/2025-03-10/tree/main)**
            
Anyway, I'm not sure what it does yet, but it must have been important to this past civilization. 
Maybe start by looking at the last two layers. 

If you do figure it out, please let us know at *archaeology@janestreet.com*.
Learn more at [janestreet.com](https://jane-st.co/3YfP5WK)

## Problem breakdown.

 - `model.pt` is a serialised PyTorch model.
 - `python arch-analysis.py` will print the architecture of the model, found in `arch.txt`.

```
Sequential(
  (0): Linear(in_features=55, out_features=224, bias=True)
  (1): ReLU()
  (2): Linear(in_features=224, out_features=232, bias=True)
  (3): ReLU()
  (4): Linear(in_features=232, out_features=64, bias=True)
  (5): ReLU()
  (6): Linear(in_features=64, out_features=208, bias=True)
  (7): ReLU()
  (8): Linear(in_features=208, out_features=200, bias=True)
  ...
  (5438): Linear(in_features=192, out_features=48, bias=True)
  (5439): ReLU()
  (5440): Linear(in_features=48, out_features=1, bias=True)
  (5441): ReLU()
)
```
 
  It's 5442 layers of a repeating [Linear perceptron](https://en.wikipedia.org/wiki/Perceptron#Definition) (Wx+b) -> ReLU pattern (activation). 
  
  The number of outputs of the layers is logged in `seq.txt`. You can get a sense of the patterns in the sequence from this bar chart of the dimensionality of each linear layer.

 ![alt text](./analysis/arch1.png)
 
 - Hypothesis 1: this model is a **neural hash function**. Some arguments why:
   - The hint says look at the last two layers. The last two layers are Linear layers with dimension of 192 and 48. These are the same sizes of hash function outputs - 192 bits, 48 bits.
   - **Evidence 1**:. Although the layers output vectors of `np.float32`, looking at the outputs they are in fact integers. See `test_hash_fn` in `js.py` to introspect these outputs. 
     - This would imply they are in fact 192 bit and 48 bit integers, suitable for a hash function.
     - **Question: are the outputs for different inputs uniformly distributed? Do they show locality (e.g. locality-sensitive hash)?**
   - **Hypothesis**: this network functions like a one-way compression function. Looking at the picture, the network has [absorbing-squeezing](https://keccak.team/sponge_duplex.html) phases where the linear dimensions are increased then reduced. The ReLu adds nonlinearity.
   - The input to this model, a vector of 55 floats, is mapped to a hash of 192 or 48 bits. Perhaps the vector is an output embedding of another model, e.g. cross-attention style.
 - Hypothesis 2: this model is a binary classifier or doing regression (predicting a single continuous value).
   - **Questions**: for what inputs does this model produce a non-zero output? (ie. not 0.0). 
   - The final Linear(48, 1) layer strongly indicates that the network's purpose is either binary classification (outputting a single logit) or regression (predicting a single continuous value). **However**, based on the purely linear architecture it feels more likely this is a red herring. Although - suitably deep neural networks can approximate any function.

Open research directions:

 1. Motifs. The network's structure (see image) is very repetitive. Ideally we can find the patterns to express it easily - though there are 5442 layers, so this is not manual labour.
    
    1. **Gemini**. I've used Google Gemini which has identified some motifs. `IB -> [A -> B -> C] * 7 -> [A' -> B -> C] * 5 -> [A'' -> B -> C] * 5 -> FB`, where `A` is a variable of some number of linear layers of different sizes. The numbers are somewhat correct (see `motif-gemini.py`), but fail to account for more than 50% of the layers.

    2. **Exhaustive search**. I've used an exhaustive search across `seq.txt` which tries to identify the hierarchical repeating motifs in the structure. This is the best I have so far - it outputs an accurate grammar of the entire neural network. Though it's not clean. 

 2. **Reverse-engineering**. 

    1. Could we see what inputs activate the model uniformly? Instead of adjusting the weights, could we compute the gradient with respect to the inputs `x` and adjust it in the direction of more activation?

## Install.

**NOTE: The .pt file requires python 3.9.**

```sh
# Install conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda

# install python3.9 (IMPORTANT FOR .PT parsing)
source $HOME/miniconda/bin/activate
conda init --all
conda create --name py39 python=3.9
conda activate py39

which -a pip
# rm any virtualenvs
# pip should only refer to 

pip install numpy torch cloudpickle
```

## Setup

1. Download `model.pt` to `js.pt`.

