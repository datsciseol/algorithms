from itertools import permutations
num = int(input())
perm_list = list(permutations(range(1, num + 1)))
length = len(perm_list)
input_list = tuple(map(int, input().split()))
idx = perm_list.index(input_list)

if idx == length - 1:
    print(-1)
else:
    print(*perm_list[idx + 1])