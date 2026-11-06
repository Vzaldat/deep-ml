import numpy as np
import re
def mmlu_letter_matching(model_outputs: list[str], ground_truth: list[str], subjects: list[str]) -> dict:
    """
    Evaluate MMLU predictions using letter-matching.
    
    Args:
        model_outputs: List of model generated responses
        ground_truth: List of correct answer letters (A, B, C, or D)
        subjects: List of subject names for each question
    
    Returns:
        Dictionary with evaluation metrics
    """
    letter = ['A', 'B', 'C', 'D']
    model_outputs = np.array(model_outputs)
    subjects = np.array(subjects)
    ground_truth = np.array(ground_truth)#
    n = len(model_outputs)
    sub_accuracy_dict : dict[str, float] = {}
    sub_count = {}
    invalid_ans = 0

    rule1_pattern = re.compile(r'^[A-Da-d]$')
    rule2_pattern = re.compile(r'^\s*\(?([A-Da-d])[.)]?\s*$')
    rule3_pattern = re.compile(r'(?:answer|choice)\s*:?\s*(?:is\s*)?\(?([A-Da-d])', re.IGNORECASE)
    rule4_pattern = re.compile(r'^[A-Da-d]')
    
    valid_letters = {'A', 'B', 'C', 'D'}

    for x in subjects:
        if x not in sub_accuracy_dict:
            sub_accuracy_dict[x] = 0.0
        if x not in sub_count:
            sub_count[x] = 0.0
        sub_count[x] += 1
    overall_accuracy = 0
    invalid_ans = 0
    for i in range(n):
        model_answer = None
        text = str(model_outputs[i]).strip()
        if rule1_pattern.match(text):
            model_answer = text.upper()
        elif match := rule2_pattern.match(text):
            model_answer = match.group(1).upper()
        elif match := rule3_pattern.search(text):
            model_answer = match.group(1).upper()
        elif match := rule4_pattern.match(text):
            model_answer = text[0].upper()
        
        if not model_answer or model_answer not in valid_letters:
            invalid_ans += 1
            model_answer = ''
        gt = str(ground_truth[i]).strip().upper()
        if model_answer and gt == model_answer:
            sub_accuracy_dict[subjects[i]] += 1 / sub_count[subjects[i]]
            overall_accuracy += 1
    
    return {
        'overall_accuracy' : overall_accuracy / n,
        'subject_accuracy' : sub_accuracy_dict,
        'valid_response_rate' : 1 - (invalid_ans / n),
        'total_correct' : overall_accuracy,
        'total_questions' : n
    }