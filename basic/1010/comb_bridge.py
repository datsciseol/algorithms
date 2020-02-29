test_case = int(input())
for _ in range(test_case):
    n, m = map(int, input().split())
    div = 1
    result = 1
    while n > 0:
        div *= n
        result *= m
        m -= 1
        n -= 1
    print(result // div)
