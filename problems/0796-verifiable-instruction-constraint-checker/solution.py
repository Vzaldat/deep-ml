import re
def check_constraints(response, constraints):
    """
    response: str — the model's generated text.
    constraints: list[str] — constraint specifications.
    Returns: dict[str, bool] mapping each constraint to whether it is satisfied,
             preserving the input order of constraints.
    """
    ans = {}
    for constraint in constraints:
        if 'word_count_min:' in constraint:
            p = response.strip().split()
            try:
                n = int(constraint[15:])
                ans[constraint] = bool(len(p) >= n)
            except (ValueError, TypeError):
                ans[constraint] = False
        elif 'word_count_max:' in constraint:
            p = response.strip().split()
            try:
                n = int(constraint[15:])
                ans[constraint] = bool(len(p) <= n)
            except (ValueError, TypeError):
                ans[constraint] = False
        elif 'contains_keyword:' in constraint:
            p = response.lower()
            try:
                n = str(constraint[17:].lower())
                ans[constraint] = bool(n in p)
            except (ValueError, TypeError):
                ans[constraint] = False
        elif 'starts_with:' in constraint:
            p = response.strip().split()
            try:
                n = str(constraint[12:])
                ans[constraint] = bool(n == p[0])
            except (ValueError, TypeError):
                ans[constraint] = False
        elif 'ends_with:' in constraint:
            p = response.strip().split()
            k = len(p)
            try:
                n = str(constraint[10:])
                ans[constraint] = bool(n == p[k - 1]) if k > 0 else False
            except (ValueError, TypeError):
                ans[constraint] = False
        elif 'no_bullet_points' in constraint:
            p = response.strip('\n')
            if p == '' or p == ' ':
                ans[constraint] = True
                continue
            ans[constraint] = not bool(re.search(r"-|\*|\d+\.", p))
        else:
            ans[constraint] = False
    return ans
