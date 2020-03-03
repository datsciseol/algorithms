num = int(input())
all_list = []
for _ in range(num):
    all_list.append(tuple(input().split()))
all_list.sort(key = lambda x : -int(x[1]))
all_list.sort(key = lambda x : int(x[2]))
all_list.sort(key = lambda x : -int(x[3]))
all_list.sort(key = lambda x : x[0])
for elem in all_list:
    print(elem[0])

