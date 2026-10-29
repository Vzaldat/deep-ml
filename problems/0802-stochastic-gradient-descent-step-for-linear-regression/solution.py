import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    m, n = X.shape
    for i in range(n_iter):
        i = i % m
        gradient = 2 * (X[i] @ weights - y[i]) * X[i]
            weights -= learning_rate * gradient
    return weights
