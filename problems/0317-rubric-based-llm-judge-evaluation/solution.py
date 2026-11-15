import numpy as np

def rubric_llm_judge_evaluation(
    judge_scores: list[list[float]],
    criteria_weights: list[float],
    passing_threshold: float = 0.6,
    max_score: float = 5.0
) -> dict:
    """
    Evaluate LLM response using rubric-based multi-judge scoring.
    
    Args:
        judge_scores: 2D list where judge_scores[i][j] is judge i's score for criterion j
        criteria_weights: Weights for each criterion (should sum to 1)
        passing_threshold: Minimum normalized score to pass (0 to 1)
        max_score: Maximum possible score for each criterion
    
    Returns:
        Dictionary with evaluation results
    """
    criterion_scores = np.mean(np.transpose(judge_scores), axis=1)
    weighted_scores = np.dot(criterion_scores, criteria_weights)
    normalised_scores = weighted_scores / max_score
    sigma_bar = np.mean(np.std(np.transpose(judge_scores), axis=1))
    judge_agreement = max(0, 1 - 2 * sigma_bar / max_score)

    return {
        "criterion_scores" : [round(float(x), 4) for x in criterion_scores],
        "weighted_score" : round(float(weighted_scores), 4),
        "normalized_score" : round(float(normalised_scores), 4),
        "pass_status" : bool(normalised_scores >= passing_threshold),
        "judge_agreement" : round(float(judge_agreement), 4)
    }
