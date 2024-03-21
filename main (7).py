
arr = [1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 1, 1, 2, 2, 3, 3, 3, 3]
count_dict = {}
for elem in arr:
    if elem in count_dict:
        count_dict[elem] += 1
    else:
        count_dict[elem] = 1
for x, y in count_dict.items():
    print(f"Элемент {y} встречается {x} раз")

