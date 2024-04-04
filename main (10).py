import numpy as np

B = np.random.randint(0, 10, size=(3, 3))

print("Матрица B:")
print(B)

z = [np.count_nonzero(row == 0) for row in B]

print("Массив из кол нулевых элементов каждой строки:")
print(z)

n = [np.count_nonzero(B[:, col]) for col in range(B.shape[1])]

print("Массив из кол ненулевых элементов каждого столбца:")
print(n)
