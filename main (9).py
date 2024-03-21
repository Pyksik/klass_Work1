
M = 4
N = 3
B = [[1, 0, 2],
     [0, 3, 4],
     [5, 0, 6],
     [0, 0, 7]]
for x in B:
    print(x)
egor = sum(1 for x in B for elem in x if elem != 0)
print(f"Количество ненулевых элементов в матрице: {egor}")
