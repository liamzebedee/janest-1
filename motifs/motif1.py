def longest_common_prefix(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return a[:i]

def find_longest_repeated_substring(seq):
    n = len(seq)
    if n < 2: 
        return None
    # Build suffix indices sorted by their suffixes
    suffix_indices = sorted(range(n), key=lambda i: seq[i:])
    lrs = []
    # Compute longest common prefix for adjacent suffixes
    for i in range(n - 1):
        s1, s2 = suffix_indices[i], suffix_indices[i+1]
        lcp = longest_common_prefix(seq[s1:], seq[s2:])
        if len(lcp) > len(lrs) and len(lcp) > 1:
            lrs = lcp
    return lrs if len(lrs) > 1 else None

def replace_substring(seq, sub, symbol):
    new_seq = []
    i = 0
    while i < len(seq):
        if seq[i:i+len(sub)] == sub:
            new_seq.append(symbol)
            i += len(sub)
        else:
            new_seq.append(seq[i])
            i += 1
    return new_seq

# Example input sequence (list of ints)
sequence = open('seq.txt', 'r').read().split(',')
grammar = {}
# Generate symbols A, B, C, ...
from string import ascii_uppercase
symbol_gen = iter(ascii_uppercase)

# Greedy replacement of the longest repeated substring.
while True:
    motif = find_longest_repeated_substring(sequence)
    if not motif:
        break
    symbol = next(symbol_gen)
    grammar[symbol] = motif
    sequence = replace_substring(sequence, motif, symbol)

print("Grammar rules (motif = expansion):")
for sym, rule in grammar.items():
    print(f"{sym} = {rule}")
print("\nCompressed sequence representation:")
print(sequence)
