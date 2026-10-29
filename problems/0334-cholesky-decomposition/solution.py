import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.
    
    Args:
        A: A symmetric positive-definite matrix (2D list or numpy array)
    
    Returns:
        L: Lower triangular matrix such that A = L @ L.T as a 2D list,
           or -1 if decomposition is not possible
    """
    # Your code here
    try:
        A = np.array(A, dtype=float)
    except:
        return -1
    
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return -1
    
    n = A.shape[0]

    if n == 0:
        return -1
    
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                sum_val = np.sum(L[i, :j] ** 2)
                val = A[i, i] - sum_val
                if val <= 0:
                    return -1
                L[i, j] = np.sqrt(val)
            else:
                sum_val = np.sum(L[i, :j] * L[j, :j])
                L[i, j] = (A[i, j] - sum_val) / L[j, j]
    return L.tolist()