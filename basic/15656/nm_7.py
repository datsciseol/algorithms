n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
result_list = []
def nm_7(num):
    if num == m:
        print(*result_list)
        return
    for iter in range(n):
        result_list.append(num_list[iter])
        nm_7(num + 1)
        result_list.pop()
        
nm_7(0)