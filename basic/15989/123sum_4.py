D = [[0, 0, 0, 0] for _ in range(10001)]
D[1] = [0, 1, 0, 0]
D[2] = [0, 1, 1, 0]
D[3] = [0, 1, 1, 1]
for iter in range(4, 10001):
    D[iter][1] = D[iter - 1][1]
    D[iter][2] = D[iter - 2][1] + D[iter - 2][2]
    D[iter][3] = D[iter - 3][1] + D[iter - 3][2] + D[iter - 3][3]
    
test_case = int(input())
for _ in range(test_case):
    print(sum(D[int(input())]))
