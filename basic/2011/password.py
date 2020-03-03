from collections import defaultdict
num_dict = defaultdict(int)
num = input()
length = len(num)
if num[0] >= '1' and num[0] <= '9':
    num_dict[1] = 1
if len(num) >= 2:
    base = int(num[0] + num[1])
    if base >= 1 and base <= 26:
        num_dict[2] = num_dict[1] + 1
    if num[1] == 0:
        num_dict[2] -= 1
    for iter in range(3, length + 1):
        if num[iter - 1] >= '1' and num[iter - 1] <= '9':
            num_dict[iter] += num_dict[iter - 1]
        if int(num[iter - 2] + num[iter - 1]) >= 1 and int(num[iter - 2] + num[iter - 1]) <= 26:
            num_dict[iter] += num_dict[iter - 2]
print(num_dict[length] % 1000000)