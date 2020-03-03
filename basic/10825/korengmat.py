num = int(input())
all_list = []
for _ in range(num):
    all_list.append(tuple(input().split()))
all_list.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for elem in all_list:
    print(elem[0])

