import sys
input = sys.stdin.readline
n, m = map(int, input().split())
check_list = [False] * n
string = list(map(int, input().rstrip().split()))
string.sort()
result_list = []
def nm_9(num):
    if num == m:
        print(*result_list)
        return
    overlap = 0
    for iter in range(n):
        if not check_list[iter] and string[iter] != overlap:
            check_list[iter] = True
            result_list.append(string[iter])
            nm_9(num + 1)
            result_list.pop()
            check_list[iter] = False
            overlap = string[iter]
nm_9(0)


# 1       2       2
# 1 2 2   1 2 2   1 2 2