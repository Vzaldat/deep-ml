import numpy as np

def correlations(x, y):
    # Return [pearson, spearman, kendall_tau_b]
    x = np.array(x)
    y = np.array(y)

    pearson_xy = _pearson(x, y)

    # spearman
    spearman_xy = _pearson(_rank(x), _rank(y))

    c, d, t_x, t_y = _CDT(x, y)
    kendall_tau = (c - d) / (np.sqrt((c + d + t_x) * (c + d + t_y)))

    return [pearson_xy, spearman_xy, kendall_tau]

def _pearson(x, y):
        return np.sum((x - np.mean(x)) * (y - np.mean(y))) / (np.sqrt((np.sum((x - np.mean(x)) ** 2))) * np.sqrt(np.sum(((y - np.mean(y)) ** 2))))

def _rank(x):
    n = len(x)
    sorted_index = sorted(range(n), key = lambda i : x[i])
    ranks = [0.0] * n

    i = 0
    while i < n:
        j = i
        while j + 1 < n and x[sorted_index[j + 1]] == x [sorted_index[i]]:
            j += 1
        avg_rank = (j + i) / 2.0 + 1.0

        for k in range(i, j + 1):
            ranks[sorted_index[k]] = avg_rank
        
        i = j + 1
    
    return ranks

def _CDT(x, y):
    c, d, t_x, t_y = 0, 0, 0, 0
    for i in range(len(x)):
        for j in range(i, len(x)):
            if (x[i] - x[j]) * (y[i] - y[j]) > 0:
                c += 1
            elif (x[i] - x[j]) * (y[i] - y[j]) < 0:
                d += 1
            else:
                if x[i] == x[j] and y[i] != y[j]:
                    t_x += 1
                elif y[i] == y[j] and x[i] != x[j]:
                    t_y += 1
    return c, d, t_x, t_y