n, m = map(int, input().split())
check_list = [False] * n
num_list = [elem + 1 for elem in range(n)]
result_list = []
def nm_dfs(num):
    if num == m:
        print(*result_list)
    for i in range(n):
        if check_list[i] == True:
            continue
        check_list[i] = True
        result_list.append(num_list[i])
        nm_dfs(num + 1)
        result_list.pop()
        check_list[i] = False
nm_dfs(0)