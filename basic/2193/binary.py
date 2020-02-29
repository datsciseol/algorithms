length = int(input())
result_list = [0] * (length + 1)
result_list[1] = 1
result_list[2] = 1
for iter in range(3, length + 1):
    result_list[iter] = result_list[iter - 1] + result_list[iter - 2]
print(result_list[length])