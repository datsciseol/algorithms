from collections import defaultdict
num_dict = defaultdict(int)
num_input = input()
if num_input[0] >= '1' and num_input[0] <= '9':
    num_dict[1] = 1
length = len(num_input)
if length >= 2:
    if int(num_input[1]) >= 1 and int(num_input[1]) <= 9:
        num_dict[2] = 1 
    if int(num_input[0] + num_input[1]) >= 10 and int(num_input[0] + num_input[1]) <= 26:
        num_dict[2] += 1
    for iter in range(3, length + 1):
        if int(num_input[iter - 1]) >= 1 and int(num_input[iter - 1]) <= 9:
            num_dict[iter] = max(num_dict[iter - 1], 1)
        if int(num_input[iter - 2] + num_input[iter - 1]) >= 10 and int(num_input[iter - 2] + num_input[iter - 1]) <= 26:
            num_dict[iter] += max(num_dict[iter - 2], 1)
print(num_dict[length] % 1000000)

# 01을 1 등으로 처리해서 가능한 모든 조합을 고려하는 코드