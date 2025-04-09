def longest_common_prefix(seq1, seq2):
    i = 0
    while i < len(seq1) and i < len(seq2) and seq1[i] == seq2[i]:
        i += 1
    return seq1[:i]

def find_longest_repeated_substring(seq):
    n = len(seq)
    # Create sorted list of suffix starting indices.
    suffix_indices = sorted(range(n), key=lambda i: seq[i:])
    lrs = ()
    for i in range(n - 1):
        s1, s2 = suffix_indices[i], suffix_indices[i+1]
        lcp = longest_common_prefix(seq[s1:], seq[s2:])
        if len(lcp) > len(lrs) and len(lcp) > 1:
            lrs = tuple(lcp)
    return lrs if len(lrs) > 1 else None

def find_all_occurrences(seq, sub):
    L = len(sub)
    occ = []
    for i in range(len(seq) - L + 1):
        if seq[i:i+L] == sub:
            occ.append(i)
    return occ

if __name__ == "__main__":
    # Example sequence (list of ints; replace with your own)
    sequence = open('seq.txt', 'r').read().split(',')
    
    # Find longest repeated motif (as a tuple)
    motif = find_longest_repeated_substring(sequence)
    if motif is None:
        print("No repeated motif found.")
    else:
        # Use a symbol to represent the motif.
        from string import ascii_uppercase
        symbol = next(iter(ascii_uppercase))
        
        # Find all (overlapping allowed) starting indices of motif.
        occ = find_all_occurrences(sequence, list(motif))
        
        print("Grammar rule:")
        print(f"{symbol} = {list(motif)}")
        print("\nOriginal sequence annotated with motif occurrences:")
        print(f"Motif {symbol} occurs at indices: {occ}")
        
        # Optionally, build an annotated representation.
        # For each index, if a motif starts there, mark it with the symbol.
        annotated = []
        L = len(motif)
        i = 0
        while i < len(sequence):
            if sequence[i:i+L] == list(motif):
                annotated.append(symbol)
                i += 1  # Advance by 1 to allow overlapping occurrences.
            else:
                annotated.append(sequence[i])
                i += 1
        print("\nAnnotated sequence (each occurrence of motif replaced by symbol):")
        print(annotated)
