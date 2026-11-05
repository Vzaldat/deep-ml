import numpy as np

def mmlu_log_prob_score(log_probs: list, correct_answers: list) -> dict:
    """
    Compute MMLU-style log-probability scoring metrics.
    
    Args:
        log_probs: List of lists, where each inner list contains 
                   log-probabilities for each answer choice
        correct_answers: List of correct answer indices (0-indexed)
    
    Returns:
        Dictionary with 'accuracy', 'predictions', and 'avg_correct_prob'
    """
    accuracy, predictions, avg_correct_prob = 0, [], 0
    n = len(log_probs)
    for i in range(n):
        denom = 0
        prob_array = np.array(log_probs[i])
        j = np.argmax(prob_array)
        max_j = np.max(prob_array)
        for x in prob_array:
            denom += np.e ** (x - max_j)
        if j == correct_answers[i]:
            accuracy += 1
        predictions.append(j)
        avg_correct_prob += (np.e ** (prob_array[correct_answers[i]] - max_j))/denom
    
    return {
        'accuracy' : accuracy / n,
        'predictions' : predictions,
        'avg_correct_prob' : avg_correct_prob / n
    }
