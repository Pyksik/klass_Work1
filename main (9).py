import numpy as np

matrix = np.random.randint(1, 100, size=(4, 4))

print("Матрица:")
print(matrix)

x = [max(col) for col in matrix.T]

print("Массив из максимальных элементов каждого столбца:")
print(x)
