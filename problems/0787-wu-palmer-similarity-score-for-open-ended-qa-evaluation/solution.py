def wups(depth_w1: int, depth_w2: int, depth_lca: int) -> float:
    """Compute Wu-Palmer Similarity between two words in a taxonomy."""
    return (2 * depth_lca) / (depth_w1 + depth_w2) if depth_w1 + depth_w2 != 0 else 0.0