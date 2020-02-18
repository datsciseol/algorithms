num = int(input())
num_list = [0] * 100001
num_list[1] = 0
num_list[2] = 1
num_list[3] = 1
num_list[4] = 2
num_list[5] = 3
for i in range(6, 100001):
    if i % 2 == 0:
        num_list[i] = num_list[i // 2] + 1
    else:
        num_list[i] = num_list[i - 1] + 1
print(num_list[num])