from collections import defaultdict
length = int(input())
num_list = [0]
num_list += list(map(int, input().split()))
dp_dict = defaultdict(int)
dp_dict[1] = num_list[1]
result = dp_dict[1]
if length >= 2:
    for iter in range(2, length + 1):
        dp_dict[iter] += max(dp_dict[iter - 1] + num_list[iter], num_list[iter])
        result = max(result, dp_dict[iter])
print(result)
    