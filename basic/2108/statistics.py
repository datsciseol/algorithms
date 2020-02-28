from collections import defaultdict
import sys
input = sys.stdin.readline
num = int(input())
num_list = []
num_dict = defaultdict(int)
for _ in range(num):
    elem = int(input())
    num_list.append(elem)
    num_dict[elem] += 1
# average_mean
print(round(sum(num_list) // num, 0))

num_list.sort()

# median
print(num_list[(num - 1) // 2])

# many
many_list = []
item = num_dict.values()
maximum = max(item)
for key, value in num_dict.items():
    if value == maximum:
        many_list.append(key)
many_list.sort()
if len(many_list) > 1:
    print(many_list[1])
else:
    print(many_list[0])

# range
print(num_list[len(num_list) - 1] - num_list[0])