import numpy as np

def standardize(arr):
    rows, columns = arr.shape
    std_arr = np.zeros((rows, columns))
    for col in range(columns):
        std_col = np.zeros((rows))
        mu = np.mean(arr[:, col])
        sd = np.std(arr[:, col])
        for row in range(rows):
            std_col[row] = (arr[row, col] - mu)/sd
            std_arr[:, col] = std_col
    return std_arr
