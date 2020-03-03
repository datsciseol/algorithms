# D[n][1] = D[n - 2][2] + D[n - 3][3]
# D[n][2] = D[n - 1][1] + D[n - 3][3]
# D[n][3] = D[n - 1][1] + D[n - 2][2]
div = 1000000009 
D = [[0, 0, 0, 0] for _ in range(100001)]
D[1] = [0, 1, 0, 0]
D[2] = [0, 0, 1, 0]
D[3] = [0, 1, 1, 1]
D[4] = [0, 2, 0, 1]
D[5] = [0, 1, 2, 1]
# D[n][k] = n을 만드는데 끝자리가 k인 경우의 수
for iter in range(6, 100001):
    D[iter][1] = (D[iter - 1][2] + D[iter - 1][3]) % div
    D[iter][2] = (D[iter - 2][1] + D[iter - 2][3]) % div
    D[iter][3] = (D[iter - 3][2] + D[iter - 3][1]) % div
test_case = int(input())
for _ in range(test_case):
    num = int(input())
    print(sum(D[num]) % div)