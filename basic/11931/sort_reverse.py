import sys
input = sys.stdin.readline
num = int(input().strip())
num_list = []
for _ in range(num):
    num_list.append(int(input().strip()))
num_list.sort(reverse = True)
for elem in num_list:
    print(elem)