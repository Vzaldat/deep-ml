def prepare_eval_input(tokens: list, mode: str, reserved_output: int) -> list:
    """
    Truncate a token list to fit the context window of the given reasoning mode.
    """
    valid_modes = {"non-think" : 8192, "high" : 131072 , "max" : 393216}
    num_input_tokens = len(tokens)
    if mode not in list(valid_modes.keys()):
        raise ValueError
    else:
        if num_input_tokens + reserved_output > valid_modes[mode]:
            length_max = valid_modes[mode] - reserved_output
            if length_max <= 0:
                return []
            elif num_input_tokens > length_max:
                return tokens[num_input_tokens - length_max : ]
            elif num_input_tokens <= length_max:
                return tokens
            else:
                return []
        else:
            return tokens
    return []