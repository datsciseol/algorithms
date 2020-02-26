def expo(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return a * (expo(a, b // 2, c) ** 2) % c
    else:
        return (expo(a, b // 2, c) ** 2) % c

a, b, c = map(int, input().split())
print(expo(a, b, c))
