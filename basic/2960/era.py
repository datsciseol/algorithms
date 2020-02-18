result_list = [1] * 1001
result_list[0] = 0
result_list[1] = 0
cnt = 0
n, k = map(int, input().split())
for num in range(2, 1001):
    if result_list[num]:
        cnt += 1
        basis = num + num
        while (basis <= 1000):
            result_list[basis] = 0
            cnt += 1
            if (cnt == k):
                print(basis)
                break
            basis += num
