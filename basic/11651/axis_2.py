num = int(input())
axis_list = []
for _ in range(num):
    axis_list.append(list(map(int, input().split())))
axis_list = sorted(axis_list, key = lambda axis : (axis[1], axis[0]) )
for elem in axis_list:
    print(*elem)
