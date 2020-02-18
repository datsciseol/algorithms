num_list = list(map(int, input().split()))
comp_list = [1, 1, 2, 2, 2, 8]
result_list = []
for i in range(6):
    result_list.append(comp_list[i] - num_list[i])
for elem in result_list:
    print(elem, end = " ")
