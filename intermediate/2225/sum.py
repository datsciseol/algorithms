# 이것으로 마지막에 꼭 나누어주기
div = 1000000000
n, k = map(int, input().split())
dp_list = [[0] * 201 for _ in range(201)]
dp_list[0] = [1] * 201
dp_list[1] = [1] * 201 
for kter in range(2, 201):
    for nter in range(201):
        for jter in range(nter + 1):
            dp_list[kter][nter] += dp_list[kter - 1][jter] % div
print(dp_list[k][n] % div)