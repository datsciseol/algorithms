from collections import defaultdict
num_dict = defaultdict(int)
length = int(input())
for _ in range(length):
    elem = int(input())
    num_dict[elem] += 1
num_items = sorted(list(num_dict.items()), key = lambda x : x[0])
for elem in num_items:
    key, value = elem[0], elem[1]
    while value > 0:
        print(key)
        value -= 1


