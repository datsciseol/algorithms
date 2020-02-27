from itertools import product
n, m = map(int, input().split())
product_list = product(range(1, n + 1), repeat = m)
for elem in product_list:
    print(*elem)