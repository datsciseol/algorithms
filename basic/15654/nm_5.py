import sys
input = sys.stdin.readline
n, m = map(int, input().split())
string = list(map(int, input().rstrip().split()))
string.sort()
result_list = []
check_list = [False] * n
def nm_dfs5(num):
    if num == m:
        print(*result_list)
    for iter in range(n):
        if check_list[iter] == True:
            continue
        check_list[iter] = True
        result_list.append(string[iter])
        nm_dfs5(num + 1)
        check_list[iter] = False
        result_list.pop()
nm_dfs5(0)

        