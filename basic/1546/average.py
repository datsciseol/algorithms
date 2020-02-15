sub_num = int(input())
num_list = list(map(int, input().split()))

num_max = max(num_list)
for i in range(len(num_list)):
    num_list[i] = num_list[i] / num_max * 100

average = sum(num_list) / sub_num
print(average)
