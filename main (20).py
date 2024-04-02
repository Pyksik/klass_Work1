import numpy as np

M = 5
matrix = np.random.randint(0, 10, (M, M))

print("Матрица:")
print(matrix)

z = [np.count_nonzero(row) for row in matrix]

print("Количество ненулевых элементов в каждой строке:")
print(z)