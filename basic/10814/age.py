total = int(input())
member_list = []
for _ in range(total):
    member_list.append(list(input().split()))
for elem in member_list:
    elem[0] = int(elem[0])
member_list.sort(key = lambda x : x[0])
for elem in member_list:
    print(*elem)