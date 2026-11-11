import numpy as np
from collections import Counter

def bleu_score(candidate: list[str], references: list[list[str]], max_n: int = 4) -> float:
    """
    Calculate BLEU score for a candidate sentence against reference sentences.
    
    Args:
        candidate: List of tokens in the candidate sentence
        references: List of reference sentences, each as a list of tokens
        max_n: Maximum n-gram order (default: 4)
    
    Returns:
        BLEU score between 0 and 1
    """
    # Your code here
    if not candidate and not references:
        return 0.0
    
    c = len(candidate)

    ref_lens = [ len(r) for r in references ]
    r = min(ref_lens, key=lambda x : (abs(x - c), x))
    
    if c > r:
        bp = 1.0
    else:
        bp = np.exp(1 - (r / c)) if c > 0 else 0.0
    
    precisions = []

    for n in range(1, max_n + 1):
        cand_ngrams = Counter(tuple(candidate[i:i+n]) for i in range(len(candidate) - n + 1))
        tot_cand_ngrams = sum(cand_ngrams.values())

        if tot_cand_ngrams == 0:
            return 0.0
        
        max_ref_counts = Counter()

        for ref in references:
            ref_ngrams = Counter(tuple(ref[i:i+n]) for i in range(len(ref) - n + 1))
            for ngram, count in ref_ngrams.items():
                max_ref_counts[ngram] = max(max_ref_counts[ngram], count)
            
        clipped_sum = 0
        for ngram, count in cand_ngrams.items():
            clipped_sum += min(count, max_ref_counts[ngram])

        precision = clipped_sum / tot_cand_ngrams

        if precision == 0.0:
            return 0.0
        precisions.append(precision)
    
    return float(bp * np.exp(np.mean(np.log(precisions))))