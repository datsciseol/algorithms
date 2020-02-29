from collections import defaultdict
def sum_dict(num_dict, num):
    num_sum = 0
    for i in range(0, num + 1):
        num_sum += num_dict[i]
    return num_sum
num_dict = {}
num = int(input())
for iter in range(0, 10):
    num_dict[iter] = 1
for jter in range(num - 1):
    temp_dict = defaultdict(int)
    for kter in range(0, 10):
        temp_dict[kter] += sum_dict(num_dict, kter) % 10007
    num_dict = temp_dict
print(sum(num_dict.values()) % 10007)
    
