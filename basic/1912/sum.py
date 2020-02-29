length = int(input())
num_list = list(map(int, input().split()))
temp_list = [0] * length
temp_list[0] = num_list[0]
if length >= 2:
    for iter in range(1, length):
        temp_list[iter] += (max(num_list[iter], temp_list[iter - 1], temp_list[iter - 1] + num_list[iter]))
print(temp_list)
        