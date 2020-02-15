import sys
test_num = int(input())

for _ in range(test_num):
    num, string = input().split()
    for elem in string:
        ans = elem * int(num)
        print(ans, end="")
    print()
