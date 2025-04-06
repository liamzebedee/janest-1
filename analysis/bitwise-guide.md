Bitwise operations in neural networks
=====================================

```
Bitstring of length 100
Each neuron represents a single bit
ie. 
1 byte = 8 bits
100 units = 100 bits
```

## Simplification rules.

### Slice mask - on.

```py
def l0_0(x):
    # x is a list (or vector) of length 55
    return max(0, 1.0*x[0])
def l0_1(x):
    # x is a list (or vector) of length 55
    return max(0, 1.0*x[1])
def l0_2(x):
    # x is a list (or vector) of length 55
    return max(0, 1.0*x[2])
def l0_3(x):
    # x is a list (or vector) of length 55
    return max(0, 1.0*x[3])
def l0_4(x):
    # x is a list (or vector) of length 55
    return max(0, 1.0*x[4])
def l0_5(x):
    # x is a list (or vector) of length 55
    return max(0, 1.0*x[5])
```

```
Simplifies to:
    b = x[0:n]
```

### Slice mask - skip.

```py
def l0_111(x):
    # x is a list (or vector) of length 55
    return max(0, 0)
```

```
Simplifies to:
    skip bit n
```

### Slice mask - skip.

```py
def l0_112(x):
    # x is a list (or vector) of length 55
    return max(0, -1.0 + 1.0*x[0])
def l0_113(x):
    # x is a list (or vector) of length 55
    return max(0, -1.0 + 1.0*x[1])
def l0_114(x):
    # x is a list (or vector) of length 55
    return max(0, -1.0 + 1.0*x[2])
def l0_115(x):
    # x is a list (or vector) of length 55
    return max(0, -1.0 + 1.0*x[3])
def l0_116(x):
    # x is a list (or vector) of length 55
    return max(0, -1.0 + 1.0*x[4])
def l0_117(x):
    # x is a list (or vector) of length 55
    return max(0, -1.0 + 1.0*x[5])
```

Simplifies to:

```
!x[0:n]
```

 - if x=1, -1 + 1 = 0
 - if x=0, -1 + 0 = -1
 - if x=-1, -1 + -1 = 0

I'm presuming in ternary, -1 is 0, and 1 is 1. 

## Bit shift.

```

```