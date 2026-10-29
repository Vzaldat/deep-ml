import numpy as np

def gradient_boosting_step(X, y, current_predictions, learning_rate=0.1):
    """
    Perform one step of gradient boosting regression using a decision stump.
    
    Args:
        X: Feature matrix (list of lists), shape (n_samples, n_features)
        y: Target values (list), shape (n_samples,)
        current_predictions: Current ensemble predictions (list), shape (n_samples,)
        learning_rate: Learning rate for the update (default 0.1)
    
    Returns:
        List of updated predictions rounded to 4 decimal places
    """
    residuals = np.array(y) - np.array(current_predictions)
    stump_predictions = []
    best_total_loss = np.inf
    best_threshold = 0
    X = np.array(X)
    n_samples, n_features = X.shape
    for feature_idx in range(n_features):
        X_col = X[:, feature_idx]
        thresholds = np.unique(X_col)
        for t in thresholds:
            left_mask = X_col <= t
            right_mask = ~left_mask

            left_val = np.mean(residuals[left_mask])
            right_val = np.mean(residuals[right_mask])

            left_sse = np.sum((residuals[left_mask] - left_val) ** 2)
            right_sse = np.sum((residuals[right_mask] - right_val) ** 2)

            total_loss = left_sse + right_sse
            if total_loss < best_total_loss:
                best_threshold = t
                best_total_loss = total_loss
                candid_preds = np.zeros(n_samples)
                candid_preds[left_mask] = left_val
                candid_preds[right_mask] = right_val
                stump_predictions = candid_preds
    
    return current_predictions + learning_rate * stump_predictions