import sys
input = sys.stdin.readline
num = input()
string = input().rstrip()
num = input()
for elem in input().rstrip().split():
    if elem != " " and elem in string:
        print(1)
    elif elem != " " and elem not in string:
        print(0)