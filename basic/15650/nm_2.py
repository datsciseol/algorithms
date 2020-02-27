from itertools import combinations
n, m = map(int, input().split())
comb_list = combinations(range(1, n + 1), m)
for elem in comb_list:
    print(*elem)
