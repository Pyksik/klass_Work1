import numpy as np

M = 3
matrix = np.random.randint(0, 10, (M, M))

print("Матрица:")
print(matrix)

x = [np.min(row) for row in matrix]

print("Минимальные элементы в каждой строке:")
print(x)