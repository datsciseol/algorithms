n, m = map(int, input().split())
num_list = [elem + 1 for elem in range(n)]
result = []
def nm3_dfs(num):
    if num == m:
        print(*result)
        return
    for i in range(n):
        result.append(num_list[i])
        nm3_dfs(num + 1)
        result.pop()
nm3_dfs(0)