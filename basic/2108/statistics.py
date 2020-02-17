num = int(input())
num_list = []
for _ in range(num):
    num_list.append(int(input()))
print("{:.1f}".format(sum(num_list) / len(num_list)))
num_list.sort()
print()
print()
print(num_list[len(num_list) - 1] - num_list[0])