from collections import defaultdict
num = int(input())
num_dict = {}
num_dict[0] = 0
for iter in range(1, 10):
    num_dict[iter] = 1
for jter in range(num - 1):
    temp_dict = defaultdict(int)
    temp_dict[0] += num_dict[1] % 1000000000
    temp_dict[9] += num_dict[8] % 1000000000
    for kter in range(1, 9):
        temp_dict[kter] += (num_dict[kter - 1] + num_dict[kter + 1]) % 1000000000
    num_dict = temp_dict
print(sum(num_dict.values()) % 1000000000)
