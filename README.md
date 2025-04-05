Dwarkesh Jane St problem
========================

This one was pretty easy

## Problem.

Today I went on a hike and found a pile of tensors hidden underneath a neolithic burial mound!
        
I sent it over to the local neural plumber, and they managed to cobble together this.

**[model.pt](https://huggingface.co/jane-street/2025-03-10/tree/main)**
            
Anyway, I'm not sure what it does yet, but it must have been important to this past civilization. 
Maybe start by looking at the last two layers. 

If you do figure it out, please let us know at *archaeology@janestreet.com*.
Learn more at [janestreet.com](https://jane-st.co/3YfP5WK)

## Install.

```sh
# Install conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda

# install python3.9 (IMPORTANT FOR .PT parsing)
source $HOME/miniconda/bin/activate
conda init --all
conda create --name py39 python=3.9

which -a pip
# rm any virtualenvs
# pip should only refer to 

pip install numpy torch cloudpickle
```

## Setup

1. Download `model.pt` to `js.pt`.
2. `python js.py`