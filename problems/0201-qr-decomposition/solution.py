import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
	"""
	Perform QR decomposition using Gram-Schmidt process.
	
	Args:
		A: An m x n matrix represented as list of lists
	
	Returns:
		Tuple of (Q, R) where Q is orthogonal and R is upper triangular
	"""
	# Your code here
	A_np = np.array(A, dtype=float)
	m, n = A_np.shape

	Q = np.zeros((m, n))
	R = np.zeros((m, n))

	for j in range(n):
		v = A_np[:, j].copy()

		for i in range(j):
			R[i, j] = np.dot(Q[:, i], A_np[:, j])
			v = v - R[i, j] * Q[:, i]
		
		R[j, j] = np.linalg.norm(v)
		Q[:, j] = v / R[j ,j]
	return Q.tolist(), R.tolist()