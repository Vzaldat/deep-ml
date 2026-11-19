def inject_reasoning_effort(messages, effort_level):
    """
    messages: list of dicts with keys 'role' and 'content'
    effort_level: one of 'low', 'medium', 'high', 'max'
    Returns: new list of message dicts with reasoning-effort system prompt injected.
    """
    new_dict_list = []
    effort_map = {
        "low" : "Reasoning effort: low. Provide concise answers with minimal deliberation.",
        "medium" : "Reasoning effort: medium. Think step by step before answering.",
        "high" : "Reasoning effort: high. Carefully decompose the problem and verify each step.",
        "max" : "Reasoning effort: max. Exhaustively decompose the problem, stress-test all edge cases, and document every intermediate step."
    }
    if messages == []:
        new_dict = {"role" : "system", "content" : effort_map[effort_level]}
        new_dict_list.append(new_dict)
        return new_dict_list
    
    if messages[0]["role"] != "system":
        new_dict = {'role' : 'system'}
        if effort_level not in ["low", "medium", "high", "max"]:
            raise ValueError
        new_dict['content'] = effort_map[effort_level]
        new_dict_list.append(new_dict)
        for x in messages[0:]:
            new_dict_list.append(x)
    else:
        temp = messages[0]['content']
        messages[0]['content'] = effort_map[effort_level] + '\n' + temp
        new_dict_list = messages.copy()
    return new_dict_list    