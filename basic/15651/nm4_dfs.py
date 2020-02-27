n, m = map(int, input().split())
check_list = [False] * n
num_list = [elem + 1 for elem in range(n)]
result_list = []
def nm4_dfs(num):
    if num == m:
        print(*result_list)
        return
    for iter in range(n):
        for j in range(iter):
            check_list[j] = True
        if check_list[iter] == True:
            continue
        check_list[iter] = True
        result_list.append(num_list[iter])
        nm4_dfs(num + 1)
        result_list.pop()
        for k in range(iter, n):
            check_list[k] = False
nm4_dfs(0)