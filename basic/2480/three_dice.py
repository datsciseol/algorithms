num_list = list(map(int, input().split()))
num_len = len(set(num_list))
result = 0
if num_len == 3:
    result = 10000 + 1000 * num_list[0]
elif num_len == 2:
    num_list.sort()
    result = 1000 + num_list[1] * 100 
elif num_len == 1:
    num_list.sort()
    result = 100 * num_list[2]
print(result)