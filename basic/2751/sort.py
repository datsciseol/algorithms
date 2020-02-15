import sys
input = sys.stdin.readline
all_num = int(input().rstrip('\n'))
sort_list = []

for _ in range(all_num):
    sort_list.append(int(input().rstrip('\n')))
sort_list.sort()
for elem in sort_list:
    print(elem)
