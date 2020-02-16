total = int(input())
result_list = []
for _ in range(total):
    result_list.append(tuple(map(int, input().split())))
result_list.sort()
for elem in result_list:
    x, y = elem
    print(x, y)
