import numpy as np

M = 4
matrix_B = np.random.randint(-10, 10, (M, M))

print("Матрица В:")
print(matrix_B)

pr = [np.prod([val for val in col if val < 0]) for col in matrix_B.T]

print("Произведения отрицательных элементов в каждом столбце:")
print(pr)