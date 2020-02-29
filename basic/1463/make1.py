num_dict = {}
num_dict[1] = 0
num_dict[2] = 1
num_dict[3] = 1
for iter in range(4, 1000001):
    ret = num_dict[iter - 1] + 1
    if iter % 6 == 0:
        num_dict[iter] = min(num_dict[iter // 2] + 1, num_dict[iter // 3] + 1, num_dict[iter - 1] + 1)
    elif iter % 3 == 0:
        num_dict[iter] = min(num_dict[iter // 3] + 1, num_dict[iter - 1] + 1)
    elif iter % 2 == 0:
        num_dict[iter] = min(num_dict[iter // 2] + 1, num_dict[iter - 1] + 1)
    else:
        num_dict[iter] = num_dict[iter - 1] + 1
num = int(input())
print(num_dict[num])