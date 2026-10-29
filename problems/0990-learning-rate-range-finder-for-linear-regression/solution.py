import numpy as np

def lr_range_finder(X, y, w0, a, b, n_steps):
    """
    Sweep learning rate from 10**a to 10**b over n_steps full-batch GD updates
    on a linear regression model (no bias). Return the list of MSE losses after
    each update.
    """
    X = np.array(X)
    y = np.array(y)
    w0 = np.array(w0)
    m, n = X.shape
    results = []
    for k in range(n_steps):
        w = w0
        lr_k = 10 ** (a + (b - a) * k / (n_steps - 1)) if n_steps != 1 else 10 ** a
        gradient = (2 / m) * X.T @ (X @ w - y)
        w -= lr_k * gradient
        mse_loss = float((1 / m) * (np.linalg.norm(X @ w - y)) ** 2)
        results.append(mse_loss)
    return results
