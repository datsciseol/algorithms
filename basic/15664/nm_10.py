n, m = map(int, input().split())
string = list(map(int, input().split()))
string.sort()
check_list = [False] * n
result_list = []


def nm_10(num):
    basis = 0
    if num == m:
        print(*result_list)
    for iter in range(n):
        if not check_list[iter] and basis != string[iter]:
            basis = string[iter]
            for j in range(iter + 1):
                check_list[j] = True
            result_list.append(string[iter])
            nm_10(num + 1)
            result_list.pop()
            for k in range(iter, n):
                check_list[k] = False
            
nm_10(0)
    