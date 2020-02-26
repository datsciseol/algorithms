from itertools import permutations

n, m = map(int, input().split())
num_list = [int(elem) for elem in range(1, n + 1)]
perm_list = permutations(num_list, m)
for elem in perm_list:
    print(elem[0])