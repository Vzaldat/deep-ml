import string

def exact_match_score(predictions: list[str], references: list[str]) -> float:
    """
    Calculate the exact match score between predictions and references.
    
    Args:
        predictions: List of predicted strings
        references: List of reference (ground truth) strings
    
    Returns:
        Exact match score as a float between 0 and 1
    """
    # Your code here
    n = len(predictions)
    if n == 0:
        return 0.0
    match_score = 0.0
    for i in range(n):
        if predictions[i] is not None and references[i] is not None:
            pred = _convert_string(predictions[i])
            ref = _convert_string(references[i])
        if pred == ref:
            match_score += 1
    
    return float(match_score / n)

    
def _convert_string(expr):
    expr = expr.lower()
    return "".join(char for char in expr if char.isalnum())