test_case = int(input())
dp_list = [0] * 1000001
dp_list[0] = 1
dp_list[1] = 1
for iter in range(2, 1000001):
    dp_list[iter] = dp_list[iter - 1] + str(iter).count('0')
for _ in range(test_case):
    n, m = map(int, input().split())
    if n == 0:
        print(dp_list[m])
    else:
        print(dp_list[m] - dp_list[n - 1])
    