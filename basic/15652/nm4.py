from itertools import combinations_with_replacement
n, m = map(int, input().split())
h_list = combinations_with_replacement(range(1, n + 1), m)
for elem in h_list:
    print(*elem)