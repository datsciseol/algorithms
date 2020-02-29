from collections import Counter
length = int(input())
num_list = []
for _ in range(length):
    num_list.append(int(input()))
num_counter = Counter(num_list)
max_num = max(num_counter.values())
key_list = []
for key, value in num_counter.items():
    if value == max_num:
        key_list.append(key)
key_list.sort()
print(key_list[0])
