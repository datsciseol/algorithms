num_list = {}
num_list[1] = 0
num_list[2] = 1
num_list[3] = 1
num_list[4] = 2
num_list[5] = 3
for iter in range(6, 1000001):
    comp_list = []
    comp_list.append(num_list[iter - 1] + 1)
    if iter % 2 == 0:
        comp_list.append(num_list[iter // 2] + 1)
    if iter % 3 == 0:
        comp_list.append(num_list[iter // 3] + 1)
    num_list[iter] = min(comp_list)
print(num_list[(int(input()))])