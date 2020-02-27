n, m = map(int, input().split())
check_list = [False] * n
num_list = [elem + 1 for elem in range(n)]
result_list = []

def nm_dfs2(num):
    if num == m:
        print(*result_list)
        return
    for iter in range(n):
        if check_list[iter] == True:
            continue
        check_list[iter] = True
        result_list.append(num_list[iter])
        nm_dfs2(num + 1)
        result_list.pop()
        for j in range(iter + 1, n):
            check_list[j] = False
nm_dfs2(0)