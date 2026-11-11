# Implement your function below.
from collections import Counter

def rouge_1_score(reference: str, candidate: str) -> dict:
    """
    Compute ROUGE-1 score between reference and candidate texts.
    
    Returns a dictionary with precision, recall, and f1.
    """
    # Your code here
    reference = reference.lower().strip().split()
    candidate = candidate.lower().strip().split()

    clipped_sum = 0.0

    cand_counter = Counter(candidate)
    ref_counter = Counter(reference)

    cand_len = len(candidate)
    ref_len = len(reference)

    for key, count in cand_counter.items():
        if key in ref_counter.keys():
            clipped_sum += min(count, ref_counter[key])

    precision = clipped_sum / cand_len
    recall = clipped_sum / ref_len
    f1 = 2 * precision * recall / (precision + recall) if precision + recall != 0 else 0.0

    return {
        "precision" : precision,
        "recall" : recall,
        "f1" : f1
    }
