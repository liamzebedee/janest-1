class Rule:
    def __init__(self, symbol, expansion):
        self.symbol = symbol
        self.expansion = expansion  # list of symbols or tokens
    def __repr__(self):
        return f"{self.symbol} -> {self.expansion}"

def sequitur(sequence):
    # Each symbol is a string (or int converted to str) for uniformity.
    seq = list(map(str, sequence))
    rules = {}
    next_rule_id = 1

    # Digram index: maps a tuple of two symbols to its position (index, rule_id)
    digrams = {}

    def add_digram(i):
        if i >= len(seq)-1:
            return True  # nothing to add
        digram = (seq[i], seq[i+1])
        if digram in digrams:
            j, _ = digrams[digram]
            if j != i:  # found a duplicate digram
                return enforce_rule(i, j)
        else:
            digrams[digram] = (i, None)
        return True

    def delete_digram(i):
        if i >= len(seq)-1:
            return
        digram = (seq[i], seq[i+1])
        if digram in digrams:
            del digrams[digram]

    def enforce_rule(i, j):
        nonlocal next_rule_id
        # Create a new rule for this repeated digram
        new_symbol = f"R{next_rule_id}"
        next_rule_id += 1
        # Record the new rule
        new_rule = Rule(new_symbol, [seq[i], seq[i+1]])
        rules[new_symbol] = new_rule

        def replace_at(pos):
            # Replace the occurrence at pos with the new symbol.
            # Remove the two symbols and insert new_symbol.
            delete_digram(pos-1)  # remove overlapping digram
            delete_digram(pos)
            seq[pos:pos+2] = [new_symbol]
            # Check surrounding digrams.
            add_digram(max(0, pos-1))
            add_digram(pos)

        # Replace both occurrences.
        # Make sure to replace the later occurrence first.
        pos1, pos2 = i, j
        if pos1 > pos2: pos1, pos2 = pos2, pos1
        replace_at(pos2)
        replace_at(pos1)
        # Remove the replaced digram from the index.
        return True

    i = 0
    while i < len(seq)-1:
        add_digram(i)
        i += 1

    return seq, rules

# Example usage:
if __name__ == "__main__":
    # Example sequence (replace with your actual output dimensions)
    sequence = open('seq.txt', 'r').read().split(',')
    
    compressed, grammar = sequitur(sequence)
    
    print("Grammar rules inferred:")
    for rule in grammar.values():
        print(rule)
    print("\nCompressed sequence representation:")
    print(compressed)
