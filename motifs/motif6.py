import collections


def exhaustive_compress(seq):
    grammar = {}
    next_sym = ord('A')
    
    def find_best(seq):
        best_sub, best_gain, best_occ = None, 0, []
        n = len(seq)
        for l in range(2, n):  # substrings of length >=2
            subs = {}
            for i in range(n - l + 1):
                sub = tuple(seq[i:i+l])
                subs.setdefault(sub, []).append(i)
            for sub, pos in subs.items():
                if len(pos) < 2:
                    continue
                # Select non-overlapping occurrences
                occ, last = [], -1
                for p in pos:
                    if p >= last:
                        occ.append(p)
                        last = p + l
                if len(occ) < 2:
                    continue
                gain = (len(occ)*l) - (l + len(occ))  # simplified gain metric
                if gain > best_gain:
                    best_gain, best_sub, best_occ = gain, sub, occ
        return best_sub, best_occ

    while True:
        sub, occ = find_best(seq)
        if not sub:
            break
        symbol = chr(next_sym)
        next_sym += 1
        grammar[symbol] = list(sub)
        l = len(sub)
        new_seq, i = [], 0
        occ_set = set(occ)
        while i < len(seq):
            if i in occ_set and tuple(seq[i:i+l]) == sub:
                new_seq.append(symbol)
                i += l
            else:
                new_seq.append(seq[i])
                i += 1
        seq = new_seq
    return seq, grammar

# Example usage:
# sequence = [1,2,3,1,2,3,1,2,3,4,5,6,4,5,6]
sequence = open('seq.txt','r').read().split(',')

compressed, gram = exhaustive_compress(sequence)
print("Compressed:", compressed)
print("Grammar:", gram)



# def repair(seq):
#     seq = list(seq)
#     rules = {}
#     next_sym = 65  # start at 'A'
#     while True:
#         pairs = collections.Counter(zip(seq, seq[1:]))
#         pair, count = max(pairs.items(), key=lambda x: x[1], default=((None,None),0))
#         if count < 2:
#             break
#         new_sym = chr(next_sym)
#         next_sym += 1
#         rules[new_sym] = pair
#         i, new_seq = 0, []
#         while i < len(seq):
#             if i < len(seq)-1 and (seq[i], seq[i+1]) == pair:
#                 new_seq.append(new_sym)
#                 i += 2
#             else:
#                 new_seq.append(seq[i])
#                 i += 1
#         seq = new_seq
#     return seq, rules

# # Example usage:
# compressed, grammar = repair(s)
# print("Compressed:", compressed)
# print("Grammar:", grammar)
