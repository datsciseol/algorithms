def gcd(a, b):
    num_list = []
    i = 1
    while (i <= b):
        if (a % i == 0 and b % i == 0):
            num_list.append(i)
            i = i + 1
        else:
            i = i + 1
    return (max(num_list))


test_num = int(input())
for _ in range(test_num):
    a, b = map(int, input().split())
    print(int(a*b / gcd(a, b)))
