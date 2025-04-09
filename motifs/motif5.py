import numpy as np
from sklearn.cluster import DBSCAN

def extract_motif_candidates(seq, L, eps):
    """
    For candidate motif length L, extract all contiguous sub-sequences
    and cluster them using DBSCAN with Euclidean distance.
    Returns a dict mapping cluster label -> {indices, motif (mean), count}.
    """
    seq_arr = np.array(seq, dtype=float)  # ensure numeric type
    n = len(seq)
    if n < L:
        return {}
    # Create sliding windows of length L.
    windows = np.lib.stride_tricks.sliding_window_view(seq_arr, window_shape=L)
    windows = windows.astype(float)  # ensure numeric
    # windows shape: (n - L + 1, L)
    clustering = DBSCAN(eps=eps, min_samples=2, metric='euclidean').fit(windows)
    labels = clustering.labels_
    motifs = {}
    unique_labels = set(labels)
    for label in unique_labels:
        if label == -1:  # noise
            continue
        indices = np.where(labels == label)[0]
        # Compute the approximate motif as the mean of windows in this cluster.
        cluster_windows = windows[indices]
        motif = cluster_windows.mean(axis=0).tolist()
        motifs[label] = {"indices": indices.tolist(), "motif": motif, "count": len(indices)}
    return motifs

def find_all_motifs(seq, L_min=3, L_max=20, eps=5.0):
    """
    For candidate motif lengths from L_min to L_max, extract and score motifs.
    Returns a dictionary with keys (L, label) and values including score, motif,
    and occurrence indices.
    """
    all_motifs = {}
    for L in range(L_min, L_max+1):
        motifs = extract_motif_candidates(seq, L, eps)
        for label, data in motifs.items():
            # Score: product of length and occurrence count.
            score = L * data["count"]
            all_motifs[(L, label)] = {"score": score, "L": L, 
                                      "indices": data["indices"], "motif": data["motif"],
                                      "count": data["count"]}
    return all_motifs

def annotate_sequence(seq, motif_info, L):
    """
    Create an annotated version of seq by marking starting indices where the
    candidate motif (of length L) occurs.
    """
    annotated = [str(s) for s in seq]
    for idx in motif_info["indices"]:
        annotated[idx] = f"[M{L}]"
    return annotated

if __name__ == "__main__":
    # Example sequence (replace with your actual output dimensions)
    sequence = open('seq.txt', 'r').read().split(',')

    
    # Parameters for candidate motif lengths and approximate matching threshold.
    L_min = 3
    L_max = 20
    eps = 5.0  # adjust tolerance as needed
    
    all_motifs = find_all_motifs(sequence, L_min, L_max, eps)
    
    # Select motifs with a high score (example: score >= 20).
    selected = {k: v for k, v in all_motifs.items() if v["score"] >= 20}
    
    print("Detected approximate motifs:")
    for key, data in sorted(selected.items(), key=lambda x: x[1]["score"], reverse=True):
        L, label = key
        print(f"Motif candidate with length {L}, label {label}:")
        print(f"  Count: {data['count']}, Score: {data['score']}")
        print(f"  Approximate motif: {np.round(data['motif'],2).tolist()}")
        print(f"  Occurs at indices: {data['indices']}\n")
    
    # Optionally annotate the sequence using one selected motif candidate.
    if selected:
        sample_key = list(selected.keys())[0]
        sample_motif = selected[sample_key]
        annotated_seq = annotate_sequence(sequence, sample_motif, sample_motif["L"])
        print("Annotated sequence (motif occurrence marked):")
        print(" ".join(annotated_seq))
