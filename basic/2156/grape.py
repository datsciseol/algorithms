length = int(input())
grape_dict = {}
for elem in range(1, length + 1):
    grape_dict[elem] = int(input())
dp_list = [0] * (10001)
dp_list[0] = 0
dp_list[1] = grape_dict[1]
if length >= 2:
    dp_list[2] = grape_dict[1] + grape_dict[2]
    for iter in range(3, length + 1):
        dp_list[iter] = max(dp_list[iter - 1], (dp_list[iter - 2] + grape_dict[iter]), (dp_list[iter - 3] + grape_dict[iter - 1] + grape_dict[iter]))
print(dp_list[length])