n, m = map(int, input().split())
num_list = list(set(map(int, input().split())))
num_list.sort()
result = []
def nm_10(num):
    if num == m:
        print(*result)
        return
    for elem in num_list:
        result.append(elem)
        nm_10(num + 1)
        result.pop()
nm_10(0)