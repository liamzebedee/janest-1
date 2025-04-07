

code:
- function calling
- loops
- bit operators

symbolic evaluator

symbolic trace
- list of [operation, input, output]. operations include [logic ops not and or nor xor, bitwise ops, identity (setting constants)
- Flattened assignments, no dependencies

neural network
- layers (linear(weights, bias), relu)






A **symbolic trace** is a flattened, explicit list of all intermediate computations in a program — like a netlist or SSA form — where every value is expressed in terms of prior values.

Here’s what a **symbolic trace of a 1-round DES/Feistel cipher** might look like at the bit level:

---

### 🧱 Input
```text
input[0..63]  // 64-bit input block
key[0..47]    // 48-bit round key
```

---

### 🧮 Symbolic Trace (bitwise logic steps)

```text
// Step 1: Split input into L and R
v0 = input[0..31]     // L0
v1 = input[32..63]    // R0

// Step 2: Expand R
v2 = expand_table(v1)        // 32 → 48 bits using fixed pattern

// Step 3: XOR with key
v3[i] = xor(v2[i], key[i])   // for i in 0..47

// Step 4: S-box lookup (8 S-boxes, 6 bits each)
v4[0..3]   = sbox0(v3[0..5])
v4[4..7]   = sbox1(v3[6..11])
...
v4[28..31] = sbox7(v3[42..47])

// Step 5: Permutation of S-box output
v5 = permute_table(v4)  // 32-bit permutation

// Step 6: XOR with L0
v6[i] = xor(v0[i], v5[i])  // new_R = L0 xor F(R0, key)

// Step 7: Swap halves
v7 = v1         // new_L = R0
v8 = v6         // new_R = L0 xor F(...)

// Step 8: Concatenate to get round1 output
output = concat(v7, v8)
```

---

### 🧠 Trace Format as Data

The trace can be represented as a flat list of operations like:

```python
[
  { "op": "xor", "inputs": ["v2_0", "key_0"], "output": "v3_0" },
  { "op": "sbox", "inputs": ["v3_0", "v3_1", ..., "v3_5"], "output": ["v4_0", "v4_1", "v4_2", "v4_3"] },
  { "op": "xor", "inputs": ["v0_0", "v5_0"], "output": "v6_0" },
  ...
]
```

Each line is a **pure expression**: deterministic, no branches, all inputs known.

---

### 🎯 Purpose of Symbolic Trace

This is the input to:
- **Logic synthesis** (e.g., convert to gates or netlists)
- **Neural circuit compiler** (e.g., emit layers for each op)
- **Proof tools** (e.g., verify cipher properties)

---

Want to see this turned directly into code that emits PyTorch layers?