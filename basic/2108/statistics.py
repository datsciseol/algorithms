from collections import Counter
import sys
input = sys.stdin.readline
def average(num_list, num):
    return int(round(sum(num_list) / num, 0))

def median(num_list, num):
    return num_list[(num - 1) // 2]

def most(num_list):
    cnt = Counter(num_list)
    max_num = max(cnt.values())
    max_list = []
    for key, value in cnt.items():
        if value == max_num:
            max_list.append(key)
    max_list.sort()
    if len(max_list) >= 2:
        return max_list[1]
    else:
        return max_list[0]

def scope(num_list):
    return num_list[len(num_list) - 1] - num_list[0]

num = int(input().rstrip())
num_list = []
for _ in range(num):
    num_list.append(int(input().rstrip()))
num_list.sort()
average_num = average(num_list, num)
median_num = median(num_list, num)
most_num = most(num_list)
scope_num = scope(num_list)
print(average_num)
print(median_num)
print(most_num)
print(scope_num)