import numpy as np

def verify_code_execution(
    test_cases: list[dict],
    numeric_tolerance: float = 1e-6
) -> dict:
    """
    Verify code execution results for a programming benchmark.
    
    Args:
        test_cases: List of dicts with keys:
            - 'expected': Expected output string
            - 'actual': Actual output string (or None if execution failed)
            - 'status': 'success', 'error', or 'timeout'
        numeric_tolerance: Tolerance for floating-point comparisons
        
    Returns:
        Dict with keys:
            - 'pass_rate': Proportion of passed tests (float, rounded to 4 decimals)
            - 'error_rate': Proportion of execution errors (float, rounded to 4 decimals)
            - 'passed_count': Number of passed tests (int)
            - 'total_count': Total number of tests (int)
            - 'verdicts': List of 'pass', 'fail', or 'error' for each test
    """
    # Your code here
    tot_count = len(test_cases)
    if tot_count == 0:
        return {
            'pass_rate':0.0,
            'error_rate':0.0,
            'passed_count':0.0,
            'total_count':0,
            'verdicts':[]
        }
    
    verdicts = []
    passed_count = 0
    error_count = 0

    for t in test_cases:
        expected, actual, status = t['expected'], t['actual'], t['status']
        if status in ('error', 'timeout'):
            verdicts.append('error')
            error_count += 1
            continue
        
        expected_str = str(expected).strip() if expected is not None else ""
        actual_str = str(actual).strip() if actual is not None else ""

        exp_num, act_num = None, None
        try:
            if expected is not None:
                exp_num = float(expected)
        except (ValueError, TypeError):
            pass
        
        try:
            if actual is not None:
                act_num = float(actual)
        except (ValueError, TypeError):
            pass
        
        if exp_num is not None and act_num is not None:
            if abs(exp_num - act_num) <= numeric_tolerance:
                verdicts.append('pass')
                passed_count += 1
            else:
                verdicts.append('fail')
                error_count += 1
        
        else:
            if expected_str == actual_str:
                verdicts.append('pass')
                passed_count += 1
            else:
                verdicts.append('fail')
                error_count += 1
    
    pass_rate = round(passed_count / tot_count, 4)
    error_rate = round(error_count / tot_count, 4)

    return {
        'pass_rate' : pass_rate,
        'error_rate' : error_rate,
        'passed_count' : passed_count,
        'tot_count' : tot_count,
        'verdicts' : verdicts
    }
