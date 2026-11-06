import regex
def extract_boxed_answer(response: str) -> str:
    """
    Extract the answer from within \boxed{...} in a model response.
    
    Args:
        response: The model's text response containing a boxed answer
    
    Returns:
        The content inside the last \boxed{}, or empty string if not found
    """
    # Your code here
    pattern = r".*(\\boxed(\{(?:[^{}]++|(?2))*\}))"

    match = regex.match(pattern, response)
    return match.group(1)[7:-1] if match else ''