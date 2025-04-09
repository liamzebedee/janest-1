import numpy as np
from collections import defaultdict

def segment_sequence(seq, block_length):
    """Split sequence into non-overlapping blocks of given length.
    If the sequence length is not an integer multiple of block_length,
    the final block will be shorter.
    """
    segments = []
    for i in range(0, len(seq), block_length):
        segments.append(seq[i:i+block_length])
    return segments

def block_distance(b1, b2):
    """Compute Euclidean distance between two blocks.
    Blocks must be of equal length.
    """
    return np.linalg.norm(np.array(b1) - np.array(b2))

def cluster_blocks(segments, threshold):
    """Cluster blocks using a simple greedy algorithm.
    Two blocks belong to the same cluster if their distance is below threshold.
    Returns a dictionary mapping cluster label to list of (index, block).
    """
    clusters = {}
    labels = [None] * len(segments)
    next_label = 0
    for i, block in enumerate(segments):
        assigned = False
        for label, rep in clusters.items():
            # rep is a representative block (here we use the first block in the cluster)
            if len(rep) == len(block) and block_distance(rep, block) < threshold:
                clusters[label].append((i, block))
                labels[i] = label
                assigned = True
                break
        if not assigned:
            # create new cluster with a new label (e.g., a letter)
            label = chr(65 + next_label)
            clusters[label] = [(i, block)]
            labels[i] = label
            next_label += 1
    return clusters, labels

# Example overall sequence: for illustration, you would replace this with your full list of output dims.
sequence = open('seq.txt', 'r').read().split(',')


# --- Step 1: Identify the unique segments (e.g. IB and FB)
# For this example, we assume the first block (IB) and the last block (FB) are unique.
# In practice you might try to detect where the pattern changes (by differences in block statistics).
# Here we choose candidate block lengths based on your observations:
ib_length = 18     # IB: first 18 numbers
fb_length = 59     # FB: last ~59 numbers

IB = sequence[:ib_length]
FB = sequence[-fb_length:]
middle = sequence[ib_length:-fb_length]

print("IB block:", IB)
print("FB block:", FB)

# --- Step 2: Segment the middle part into blocks.
# The overall structure suggests repeating groups like [A->B->C] or variants.
# Here we choose a candidate block length. For instance, if A, B, C blocks have lengths ~19, 14, and 12,
# then one full group might be 19+14+12 = 45 elements.
group_length = 45  
groups = segment_sequence(middle, group_length)

print("\nFound", len(groups), "groups of approximate length", group_length)

# --- Step 3: Within each group, try to segment into individual blocks.
# For illustration, we assume each group is three blocks with candidate lengths from your notes.
candidate_lengths = [19, 14, 12]  # approximate lengths for A, B, C (or variants)

def segment_group(group, candidate_lengths):
    segments = []
    idx = 0
    for cl in candidate_lengths:
        segments.append(group[idx:idx+cl])
        idx += cl
    return segments

all_group_segments = [segment_group(group, candidate_lengths) for group in groups if len(group) >= sum(candidate_lengths)]

# --- Step 4: Cluster similar blocks across groups.
# We'll cluster each block position separately (i.e. all first blocks, all second blocks, etc.)
clusters_all = {}
for pos in range(len(candidate_lengths)):
    # extract the pos-th block from each group
    blocks = [group[pos] for group in all_group_segments if len(group) > pos]
    clusters, labels = cluster_blocks(blocks, threshold=30)  # threshold chosen empirically
    clusters_all[pos] = clusters
    print(f"\nBlock position {pos} clusters:")
    for label, members in clusters.items():
        print(f"  {label}: {len(members)} occurrences")
        
# --- Step 5: Output an algebraic description.
# For example, if for block position 0 we have a dominant cluster labeled 'A',
# for block position 1 a cluster 'B', and for position 2 a cluster 'C',
# and if these clusters repeat in groups, you can describe the overall model as:
#   IB -> [A -> B -> C] * (# groups) -> FB

# Here we simply output the counts per cluster per position:
print("\nAlgebraic summary:")
print("IB -> ", end="")
group_summary = []
for pos in range(len(candidate_lengths)):
    cluster_counts = {label: len(members) for label, members in clusters_all[pos].items()}
    group_summary.append(f"Block{pos}:{cluster_counts}")
print(" -> ".join(group_summary), end=" -> FB\n")
