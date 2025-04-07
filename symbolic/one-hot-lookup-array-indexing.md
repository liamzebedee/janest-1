You can think of array indexing as selecting one element out of many using a one-hot vector—a vector where only one entry is 1 and the rest are 0.

```c
int arr[4] = {10, 20, 30, 40};
int i = 2;
int val = arr[i];
```

arr[i]
arr[i=2]


arr = [10, 20, 30, 40]
i   = [0, 0, 1, 0]

[10, 20, 30, 40]
× [ 0,  0,  1,  0]
= [ 0,  0, 30,  0]

arr[i] = arr * i = 30






val = sum(one_hot[i] * arr[i] for all i)
