from collections import defaultdict
num = int(input())
num_dict = defaultdict(int)
for _ in range(num):
    num_dict[int(input())] += 1
max_num = max(num_dict.values())
num_items = sorted(list(num_dict.items()), key = lambda x : x[0])
for elem in num_items:
    if elem[1] == max_num:
        print(elem[0])
        break
