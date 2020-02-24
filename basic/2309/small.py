small_list = []
for _ in range(9):
    small_list.append(int(input()))
basis = sum(small_list) - 100
answer_list = []
for elem1 in small_list:
    for elem2 in small_list:
        if elem1 != elem2:
            if (elem1 + elem2 == basis):
                answer_list.append((elem1, elem2))
e1, e2 = answer_list[0]
small_list.remove(e1)
small_list.remove(e2)
small_list.sort()
for elem in small_list:
    print(elem)