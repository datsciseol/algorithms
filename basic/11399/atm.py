num = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
num_sum = 0

for i in range(1, num):
    print(num_sum)
    num_sum += sum(num_list[: i])
print(num_sum)