num = int(input())
check_list = [False] * num
num_list = [elem + 1 for elem in range(num)]
result = []
def depth_fs(n):
    if n == num:
        print(*result)
    for iter in range(num):
        if not check_list[iter]:
            check_list[iter] = True
            result.append(num_list[iter])
            depth_fs(n + 1)
            result.pop()
            check_list[iter] = False
depth_fs(0)