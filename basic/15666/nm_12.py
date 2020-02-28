n, m = map(int, input().split())
num_list = list(set(map(int, input().split())))
num_list.sort()
result_list = []
check_list = [False] * n
basis = 0
def nm_12(num, basis):
    if num == m:
        print(*result_list)
        return
    for elem in num_list:
        if basis <= elem:
            basis = elem
            result_list.append(elem)
            nm_12(num + 1, basis)
            result_list.pop()
nm_12(0, basis)