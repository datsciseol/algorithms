import sys
input = sys.stdin.readline
num = int(input())
num_list = list(map(int, input().rstrip().split()))
D = [[0] * (num + 1) for _ in range(num + 1)]
max_list = [0] * (num + 1)
D[1][1] = num_list[0]
max_list[1] = num_list[0]
if num >= 2:
    D[2][1] = D[1][1] + num_list[0]
    D[2][2] = num_list[1]
    max_list[2] = max(D[2])
    for iter in range(3, num + 1):
        for jter in range(1, iter + 1):
            D[iter][jter] = max_list[iter - jter] + num_list[jter - 1]
        max_list[iter] = max(D[iter])
print(max(D[num]))



# D[n][1] = max(D[n - 1]) + num_list[1]
# D[n][2] = max(D[n - 2]) + num_list[2]
# D[n][3] = max(D[n - 3])
# .
# .
# .
# D[n][n] = num_list[n]
# D[n] = max(D[n])