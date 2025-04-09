val = sum(one_hot[i] * arr[i] for all i)

You can think of array indexing as selecting one element out of many using a one-hot vector—a vector where only one entry is 1 and the rest are 0.

```c
int arr[4] = {10, 20, 30, 40};
int i = 2;
int val = arr[i];
```

arr[i]
arr[i=2]

```
arr = [10, 20, 30, 40]
i   = [0, 0, 1, 0]
```

```c
// One hot lookup.
[10, 20, 30, 40]    
× [ 0,  0,  1,  0]  
= [ 0,  0, 30,  0]  
```

arr[i] = arr * i = 30

## Simple case.

How do we do one-hot lookup inside a neural network?
Basically:

```py
a = [5,10,15,20,25]
i = 3
# a[3] == 20

# LAYER 1
# store a in neurons 1-5
y[0] = 5
y[1] = 10
y[2] = 15
y[3] = 20
y[4] = 25

# store b in neuron 6
y[5] = 3

# LAYER 2
# matmul a*i to get a[i]
y[0] = 0 * x[0] + 0 * x[1] + 0 * x[2] + 1 * x[3] + 0 * x[4] 
# y[0] = 0 + 0 + 0 + 20 + 0 * 0 
# y[0] = 20
```

## Binary case.

This gets harder when the digits are binary.

```py
a = [5,10,15,20,25]
i = 3


# weight = 2*bit - 1 
# weight = +1 if bit==1, -1 if bit==0
# bias   = n_bits - 0.5  # activate if at least one bit
# 

# we are setting the 64 bits
# sp[i]
# i : u6  stored at 0:5
# sp: u64 stored at 6:70

# val = sum(one_hot[i] * arr[i] for all i)

# in essence:
# y[0] = 
    # select 1 bit of x using weights (1,-1,-1,-1,-1)
    # multiply by sp[0]
    # subtract all bits of x minus 0.5 to only activate for one bit
# do this for all y[0] to y[64] (size of sp)
# in order to set outputs to the bits of sp[i]

y[0] = 0 * x[0] + 0 * x[1] + 0 * x[2] + 0 * x[3] + 0 * x[4] + 0 * x[5]
# for i in range(64):
    # We can't do this! Because we can only do Wx. we cannot refer to x.
    # y[i] = x[0] * x[0 + i] + x[1] * x[1 + i] + x[2] * x[2 + i] + x[3] * x[3 + i] + x[4] * x[4 + i] + x[5] * x[5 + i]
```

