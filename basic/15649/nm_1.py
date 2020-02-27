from itertools import permutations
n, m = map(int, input().split())
perm_list = permutations(range(1, n + 1), m)
for elem in perm_list:
    print(*elem)

