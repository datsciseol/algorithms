num = int(input())
num_list = list(set(map(int, input().split())))
num_list.sort()
for elem in num_list:
    print(elem, end = " ")