import sys
input = sys.stdin.readline
num = int(input().rstrip("\n"))
num_list = list(map(int, input().rstrip("\n").split()))

mum = int(input())
mum_list = list(map(int, input().rstrip("\n").split()))

for elem in mum_list:
    if (elem in num_list):
        print("1")
    else:
        print("0")