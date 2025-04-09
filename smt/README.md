SMT solver
=============

```py
#!/bin/bash
# conda activate py39
echo solving...
set -ex


# Download the jane street model.pt
# put it in /js.pt (project root)


# 1. Install Gurobi.
# ====================

# Download for macOS and install.
# https://www.gurobi.com/downloads/older-versions-gurobi-software/

# Setup environment variables.
export GUROBI_HOME="/Library/gurobi1102/macos_universal2"
export PATH="${PATH}:${GUROBI_HOME}/bin"
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"
export GRB_LICENSE_FILE=$HOME/gurobi.lic

# Activate license.
gurobi_cl activate


# 2. Compile Marabou.
# =====================

git clone https://github.com/NeuralNetworkVerification/Marabou
cd Marabou
mkdir build
cd build
cmake ../ -DENABLE_GUROBI=ON -DRUN_UNIT_TEST=OFF -DBUILD_PYTHON=OFF
make -j32 Marabou VERBOSE=1


# 2. Compile network to simplified ONNX.
# ========================================

cd js-slice
python smtsolver.py


# 3. Run Marabou.
# =================

# Command outputted in previous step.
```