import numpy as np


def submission_score(outcomes, penalty_medians):
    """
    Score of a submission sequence (booleans, in order): penalty_medians[min(k, len - 1)] for the first
    solved submission after k failures, else 0.0. Report section 5.3.1.
    """
    for i in range(len(outcomes)):
        if outcomes[i] == True:
            return float(penalty_medians[i]) if i < len(penalty_medians) else float(penalty_medians[-1])
    return 0.0

def contest_rank(score, human_scores):
    """
    1 + number of human contest scores strictly greater than score.
    """
    for i in range(len(human_scores)):
        if human_scores[i] <= score:
            return 1 + i
    return len(human_scores)


def performance_rating(rank, human_ratings, lo=0.0, hi=4000.0, iters=50):
    """
    Rating R with seed(R) = 1 + sum_j 1 / (1 + 10 ** ((R - r_j) / 400)) equal to rank,
    by `iters` bisection steps on [lo, hi]; returns the final midpoint.
    """
    if rank > len(human_ratings):
        return 0.0
    for _ in range(iters):
        mid = (lo + hi) / 2
        seed = 1 + sum(1 / (1 + 10 **((mid - r_j) / 400)) for r_j in human_ratings)
        if seed > rank:
            lo = mid
        else:
            hi = mid

    return (lo + hi) / 2
        


def estimate_elo(results, penalty_medians, human_scores, human_ratings, n_samples=100, n_pick=10, seed=0):
    """
    Monte-Carlo expected rating: n_samples contests, each sampling n_pick of the candidates per problem
    without replacement in random order with np.random.default_rng(seed).
    Returns {"expected_rating", "mean_score", "min_rating", "max_rating"} rounded to 2 decimals.
    """
    rng = np.random.default_rng(seed)
    
    ratings = []
    scores = []
    if results is None:
        return {
            "expected_rating" : 0.0,
            "mean_score" : 0.0,
            "min_rating" : 0.0,
            "max_rating" : 0.0
        }
    for _ in range(n_samples):
    
        contest_scores = 0.0
    
        for p in range(len(results)):
            candids_array = np.array(results[p])
            num_candids = len(results[p])
            sub_order = rng.permutation(num_candids)[:min(n_pick, num_candids)]

            outcomes_p = candids_array[sub_order]
            
            scores_p = submission_score(outcomes_p, penalty_medians[p])
            contest_scores += scores_p

            rank = contest_rank(contest_scores, human_scores)
            rating = performance_rating(rank, human_ratings)
        
        ratings.append(rating)
        scores.append(contest_scores)
    
    if np.sum(scores) == 0 and 0 not in human_scores:
        ratings = [0] * n_samples    

    return {
        "expected_rating" : round(float(np.mean(ratings)), 2),
        "mean_score" : round(float(np.mean(scores)), 2),
        "min_rating" : round(float(np.min(ratings)), 2),
        "max_rating" : round(float(np.max(ratings)), 2),
    }