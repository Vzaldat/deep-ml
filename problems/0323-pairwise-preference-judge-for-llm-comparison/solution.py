def pairwise_preference_judge(comparisons: list, criteria_weights: dict, tie_threshold: float) -> dict:
    """
    Analyze pairwise comparisons between LLM responses.
    
    Args:
        comparisons: List of comparison dicts with 'id', 'scores_a', 'scores_b'
        criteria_weights: Dict mapping criterion names to importance weights
        tie_threshold: Maximum difference to declare a tie
    
    Returns:
        Dict with 'results', 'win_rate_a', 'win_rate_b', 'tie_rate', 'avg_margin'
    """
    # Your code here
    results = []
    win_rate_a = 0
    win_rate_b = 0
    tie_rate = 0
    avg_margin = 0
    if comparisons == []:
        return {
            'results': [],
            'win_rate_a': 0,
            'win_rate_b' : 0,
            'tie_rate' : 0,
            'avg_margin' : 0
        }
    count = 0
    for comp in comparisons:
        id_ = comp['id']
        count += 1
        add_dict = {
            'id' : id_,
            'winner' : '',
            'margin' : 0.0
        }
        scores_a_values = list(comp['scores_a'].values())
        scores_b_values = list(comp['scores_b'].values())
        weights_list = list(criteria_weights.values())
        sum_weights = sum(weights_list)
        a_score = 0
        b_score = 0
        for i in range(len(scores_a_values)):
            a_score += round(weights_list[i] * scores_a_values[i] / sum_weights, 4)
            b_score += round(weights_list[i] * scores_b_values[i] / sum_weights, 4)
        if a_score - b_score > tie_threshold:
            add_dict['winner'] = 'A'
            win_rate_a += 1
        elif b_score - a_score > tie_threshold:
            add_dict['winner'] = 'B'
            win_rate_b += 1
        else:
            add_dict['winner'] = 'tie'
            tie_rate += 1
        
        add_dict['margin'] = round(abs(a_score - b_score), 4)
        avg_margin += add_dict['margin']

        results.append(add_dict)
    
    return {
        'results' : results,
        'win_rate_a' : round(win_rate_a / count, 4),
        'win_rate_b' : round(win_rate_b / count, 4), 
        'tie_rate' : round(tie_rate / count, 4),
        'avg_margin' : round(avg_margin / count, 4)
    }