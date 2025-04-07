import torch.nn as nn

def generate_var_map_from_single_layer(layer):
    in_features = layer.in_features
    out_features = layer.out_features

    return {
        "inputs": [f"x{i}" for i in range(in_features)],
        "outputs": [f"y{i}" for i in range(out_features)]
    }



def generate_var_map_from_layers(layers):
    var_ids = set()
    for layer in layers:
        var_ids.update(layer.inputs)
        var_ids.add(layer.output)

    var_map = {}
    for idx, var_id in enumerate(sorted(var_ids)):
        var_map[f'v{idx}'] = var_id

    # Reverse it so we can map ID → name in decompilation
    return {v: k for k, v in var_map.items()}


import torch.nn as nn



import re

def extract_index(varname):
    # Extracts the numeric index from a variable name like "x56"
    m = re.match(r'x(\d+)', varname)
    return int(m.group(1)) if m else None




def decompile_layer(layer: nn.Linear):
    in_features = layer.in_features
    out_features = layer.out_features

    # Generate var names: x0, x1, ..., y0, y1, ...
    input_vars = [f"x{i}" for i in range(in_features)]
    output_vars = [f"y{i}" for i in range(out_features)]

    results = []

    for i in range(out_features):
        weights = layer.weight[i].detach().tolist()
        bias = layer.bias[i].item() if layer.bias is not None else 0.0

        nonzero = [(input_vars[j], w) for j, w in enumerate(weights) if w != 0]
        out = output_vars[i]

        # --- Constant Injection ---
        if not nonzero:
            if bias == 0.0:
                results.append(f"{out} = 0  # constant zero")
            elif bias == 1.0:
                results.append(f"{out} = 1  # constant one")
            else:
                results.append(f"{out} = {bias}  # literal constant")
            continue

        # --- Buffer ---
        if len(nonzero) == 1 and nonzero[0][1] == 1.0 and bias == 0.0:
            results.append(f"{out} = {nonzero[0][0]}")
            continue

        # --- NOT ---
        if len(nonzero) == 1 and nonzero[0][1] == -1.0 and bias == 1.0:
            results.append(f"{out} = not {nonzero[0][0]}")
            continue

        # --- AND ---
        if len(nonzero) == 2 and all(w == 1.0 for _, w in nonzero) and bias == -1.0:
            a, b = [v for v, _ in nonzero]
            results.append(f"{out} = {a} and {b}")
            continue

        # --- OR ---
        if len(nonzero) == 2 and all(w == 1.0 for _, w in nonzero) and bias == 0.0:
            a, b = [v for v, _ in nonzero]
            results.append(f"{out} = {a} or {b}")
            continue

        # --- XOR ---
        if len(nonzero) == 2 and all(w == -1.0 for _, w in nonzero) and bias == 1.0:
            a, b = [v for v, _ in nonzero]
            results.append(f"{out} = {a} ^ {b}")
            continue

        # --- Popcount Comparator ---
        if all(w == 1.0 for _, w in nonzero) and bias <= 0.0:
            threshold = int(-bias)
            vars_ = [v for v, _ in nonzero]
            results.append(f"{out} = popcount({', '.join(vars_)}) >= {threshold}")
            continue

        # --- Bitwise Value Comparator ---
        powers = [2 ** i for i in range(len(nonzero))]
        actual_weights = [w for _, w in nonzero]
        if actual_weights == powers:
            vars_ = [v for v, _ in nonzero]
            threshold = int(-bias)
            results.append(f"{out} = value({', '.join(vars_)}) >= {threshold}")
            continue
        
        # --- Popcount Difference Comparator ---
        # group_a = [v for v, w in nonzero if w == 8.0]
        # group_b = [v for v, w in nonzero if w == -8.0]

        # if len(group_a) > 0 and len(group_b) > 0 and len(nonzero) == len(group_a) + len(group_b) and bias == 0.0:
        #     results.append(f"{out} = popcount({', '.join(group_a)}) > popcount({', '.join(group_b)})")
        #     continue
        
        # --- Popcount Comparator Cascade (B > A + optional carry-in) ---
        pos_inputs = [v for v, w in nonzero if w == 1.0]
        neg_inputs = [v for v, w in nonzero if w == -1.0]

        # Check if bias is exactly +1.0, and there's one extra 1.0-weighted input (carry)
        if bias == 1.0 and len(pos_inputs) == len(neg_inputs) + 1:
            carry_in = None
            for v in pos_inputs:
                if v not in neg_inputs:
                    carry_in = v
                    break

            if carry_in:
                group_a = sorted(neg_inputs)
                group_b = sorted([v for v in pos_inputs if v != carry_in])
                results.append(
                    f"{out} = (popcount({', '.join(group_b)}) > popcount({', '.join(group_a)})) or {carry_in}"
                )
                continue
        
        # --- Popcount Comparator Cascade with multiple carry-in ---
        pos_inputs = [v for v, w in nonzero if w == 1.0]
        neg_inputs = [v for v, w in nonzero if w == -1.0]

        print(
            len(pos_inputs),
            len(neg_inputs),
            len(nonzero),
            bias
        )
        
        # valid if pos_inputs ⊇ neg_inputs, bias == 0, and len(neg) matches A group size
        if bias == 0.0 and set(neg_inputs).issubset(set(pos_inputs)):
            carry_terms = [v for v in pos_inputs if v not in neg_inputs]
            group_a = sorted(neg_inputs)
            group_b = sorted([v for v in pos_inputs if v not in carry_terms])
            if len(group_a) == len(group_b):  # strict A == B group size
                carry_expr = " or ".join(carry_terms)
                logic_expr = f"popcount({', '.join(group_b)}) > popcount({', '.join(group_a)})"
                if carry_terms:
                    results.append(f"{out} = {logic_expr} or {carry_expr}")
                else:
                    results.append(f"{out} = {logic_expr}")
                continue
        
        
        # --- General Scaled Bitfield Comparator ---
        if len(nonzero) == 4 and bias == 0.0:
            # Extract the weights and variable names.
            a, b, c, d = [w for _, w in nonzero]
            v0, v1, v2, v3 = [v for v, _ in nonzero]
            # Check for the pattern: b == d and c == -2*b.
            if d == b and c == -2 * b:
                # Extract numeric indices from variable names.
                indices = [extract_index(v) for v, _ in nonzero]
                diff = indices[1] - indices[0]
                if indices[2] == indices[0] + 2 * diff and indices[3] == indices[0] + 3 * diff:
                    # Emit symbolic expression.
                    results.append(f"{out} = (({v1} + {v3}) > {v2}) or {v0}")
                    continue
        
        # --- Popcount Comparator Cascade (simple case) ---
        pos_inputs = [v for v, w in nonzero if w == 1.0]
        neg_inputs = [v for v, w in nonzero if w == -1.0]
        if bias == 1.0 and len(pos_inputs) == len(neg_inputs) + 1:
            # Find the extra (carry) input.
            carry_in = None
            for v in pos_inputs:
                if v not in neg_inputs:
                    carry_in = v
                    break
            if carry_in:
                group_a = sorted(neg_inputs, key=extract_index)
                group_b = sorted([v for v in pos_inputs if v != carry_in], key=extract_index)
                results.append(
                    f"{out} = (popcount({', '.join(group_b)}) > popcount({', '.join(group_a)})) or {carry_in}"
                )
                continue
        
        # --- Extended Popcount Comparator Cascade ---
        # We assume all nonzero weights are exactly ±1.0.
        if bias in (0.0, -1.0) and all(w in (-1.0, 1.0) for _, w in nonzero):
            pos_inputs = [v for v, w in nonzero if w == 1.0]
            neg_inputs = [v for v, w in nonzero if w == -1.0]
            pos_sorted = sorted(pos_inputs, key=extract_index)
            neg_sorted = sorted(neg_inputs, key=extract_index)
            if len(pos_sorted) == len(neg_sorted):
                # No extra carry.
                results.append(f"{out} = popcount({', '.join(pos_sorted)}) > popcount({', '.join(neg_sorted)})")
                continue
            elif len(pos_sorted) == len(neg_sorted) + 1:
                # Extra positive term serves as carry.
                # Assume the highest-indexed positive is the carry.
                carry = pos_sorted[-1]
                main_pos = pos_sorted[:-1]
                results.append(f"{out} = (popcount({', '.join(main_pos)}) > popcount({', '.join(neg_sorted)})) or {carry}")
                continue

        # --- Extended Popcount Comparator Cascade (with bias -1.0) ---
        # Match when all nonzero weights are ±1.0, bias is -1.0, and there are many inputs.
        if bias == -1.0 and all(w in (-1.0, 1.0) for _, w in nonzero) and len(nonzero) > 4:
            groupA = sorted([v for v, w in nonzero if w == -1.0], key=extract_index)
            groupB = sorted([v for v, w in nonzero if w == 1.0], key=extract_index)
            # Expect groupB to be either the same size as groupA or one larger.
            if len(groupB) == len(groupA) or len(groupB) == len(groupA) + 1:
                carry_expr = ""
                main_groupB = groupB
                if len(groupB) == len(groupA) + 1:
                    # Treat the last element as a carry.
                    carry_expr = " or " + groupB[-1]
                    main_groupB = groupB[:-1]
                expr = f"popcount({', '.join(main_groupB)}) > popcount({', '.join(groupA)})"
                results.append(f"{out} = {expr}{carry_expr}")
                continue

        # --- Fallback ---
        expr = " + ".join(f"{w}*{v}" for v, w in nonzero)
        results.append(f"{out} = relu({expr} + {bias})  # unknown pattern")

    return results




# test.
import torch
model = torch.load("js.pt")

def liststrn(l):
    return "\n".join(str(x) for x in l)

test_cases = [4,2]

# decompile the model.
layer = model[0]
var_map = generate_var_map_from_single_layer(layer)
print(liststrn(decompile_layer(layer)))
