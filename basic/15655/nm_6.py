n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
check_list = [False] * n
result_list = []
def nm_6_dfs(num):
    if num == m:
        print(*result_list)
        return
    for iter in range(n):
        if check_list[iter] == True:
            continue
        for i in range(iter + 1):
            check_list[i] = True
        result_list.append(num_list[iter])
        nm_6_dfs(num + 1)
        result_list.pop()
        for j in range(iter, n):
            check_list[j] = False
    
nm_6_dfs(0)