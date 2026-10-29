import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    """
    X_B = X[batch_indices]
    y_B = y[batch_indices]
    m, n = X_B.shape
    gradient_weights = (2 / m) * X_B.T @ (X_B @ weights + bias - y_B)
    gradient_bias = (2 / m) * np.sum(X_B @ weights + bias - y_B)
    weights -= lr * gradient_weights
    bias -= lr * gradient_bias
    return np.append(weights, bias)