import numpy as np

B = np.random.randint(-10, 10, size=(3, 3))

print("Матрица B:")
print(B)

y = []
for j in range(B.shape[1]):
    x = 1
    for i in range(B.shape[0]):
        if B[i][j] > 0:
            x *= B[i][j]
    y.append(x)

print("Массив с произведениями положительных элементов каждого столбца:")
print(y)


