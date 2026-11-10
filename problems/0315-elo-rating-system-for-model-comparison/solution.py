import numpy as np

def elo_rating_update(ratings: dict, matches: list, k_factor: float) -> dict:
    """
    Update Elo ratings based on pairwise comparison results.
    
    Args:
        ratings: Dictionary mapping model names to their current Elo ratings
        matches: List of tuples (model_a, model_b, result) where result is 'a', 'b', or 'draw'
        k_factor: The K-factor controlling rating update magnitude
    
    Returns:
        Dictionary with updated ratings for all models
    """
    for m in matches:
        team1, team2, winner = m
        expected_score_a = 1 / (1 + 10 ** ((ratings[team2] - ratings[team1]) / 400))
        expected_score_b = 1 - expected_score_a
        if winner == 'draw':
            ratings[team1] += k_factor * (0.5 - expected_score_a)
            ratings[team2] += k_factor * (0.5 - expected_score_b)
        elif winner == 'a':
            ratings[team1] += k_factor * (1.0 - expected_score_a)
            ratings[team2] += k_factor * (0.0 - expected_score_b)
        else:
            ratings[team1] += k_factor * (0.0 - expected_score_a)
            ratings[team2] += k_factor * (1.0 - expected_score_b)
    
    return ratings