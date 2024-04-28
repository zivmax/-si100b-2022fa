import numpy.matlib
import numpy as np
matrix = eval(input())
rows, cols = len(matrix), len(matrix[0])
matrix = np.array(matrix)
matrix1 = matrix[::2, ::2]
matrix1 = matrix1.tolist()
print(matrix1)
matrix = matrix.tolist()
matrix2 = np.zeros((rows-2, cols-2)).astype(int)
for hang in range(0, rows-2):
    for lie in range(0, cols-2):
        matrix2[hang][lie] = (matrix[hang][lie] + matrix[hang][lie+1]+matrix[hang][lie+2] +
                              matrix[hang+1][lie] + matrix[hang+1][lie+1] + matrix[hang+1][lie+2] +
                              matrix[hang+2][lie] + matrix[hang+2][lie+1] + matrix[hang+2][lie+2]) // 9
print(matrix2.tolist())
matrix = np.array(matrix)
matrix3 = matrix
previous_sum = 0
hist = []
for k in range(0, 16):
    sum_of_matrix = np.sum((16*k <= matrix3) & (matrix3 < 16*k+16))
    hist.append(sum_of_matrix)
print(hist)