import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    # Your code here
    X = np.array(X)
    m, n = X.shape
    y = np.array(y)
    weights = np.array(weights)

    if method == "batch":
        for _ in range(n_epochs):
            gradient = (2 / m) * X.T @ (X @ weights - y)
            weights -= learning_rate * gradient
    elif method == "stochastic":
        for _ in range(n_epochs):
            for i in range(m):
                xi = X[i]
                yi = y[i]
                gradient = 2 * (np.dot(xi, weights) - yi) * xi
                weights -= learning_rate * gradient
    
    elif method == "mini_batch":
        for _ in range(n_epochs):
            # indices = np.arange(m)
            # np.random.shuffle(indices)
            # X_shuffled = X[indices]
            # y_shuffled = y[indices]

            for i in range(0, m, batch_size):
                X_batch = X[i:i+batch_size]
                y_batch = y[i:i+batch_size]

                if len(X_batch) == 0:
                    break
                
                gradient = (2 / len(X_batch)) * X_batch.T @ (X_batch @ weights - y_batch)
                weights -= learning_rate * gradient
    
    else:
        raise ValueError("method must be 'batch", 'stochastic' or 'mini_batch')
    
    return weights