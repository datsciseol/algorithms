num = int(input())
num_list = list(map(int, input().split()))
ret = 0
if len(num_list) == 1:
    ret = num_list[0] * num_list[0]
else:
    num_list.sort()
    ret = num_list[0] * num_list[-1]
print(ret)