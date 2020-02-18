n, k = map(int, input().split())
num_list = [1] * (n + 1)
num_list[0] = 0
num_list[1] = 0
cnt = 0
ans = 0
for i in range(2, n + 1):
    basis = i
    while (basis <= n):
        if (cnt == k):
            break
        if num_list[basis]:
            ans = basis
            num_list[basis] = 0
            cnt += 1
        basis += i  
print(ans)
