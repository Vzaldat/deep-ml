def macro_average_accuracy(subtask_results: dict) -> float:
    """
    Compute the unweighted macro-average accuracy across benchmark subtasks.
    Each value in subtask_results is a list of (prediction, label) tuples.
    Return the macro-average accuracy rounded to 4 decimals.
    """
    pred_label_list = list(subtask_results.values())
    total_values = len(pred_label_list)
    if total_values == 0:
        return 0
    avg_acc = 0.0
    for i in pred_label_list:
        temp_acc = 0.0
        n = len(i)
        if n == 0:
            continue
        for j in i:
            if j is not None:
                pred, label = j
            else:
                continue
            if pred == label:
                temp_acc += 1
        avg_acc += float(temp_acc / n)
    return float(avg_acc / total_values)
        