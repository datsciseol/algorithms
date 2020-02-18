import sys
input = sys.stdin.readline
num_min, num_max = map(int, input().split())
cnt = 0
num_list = [1] * 1000001
num_list[0] = 0
num_list[1] = 0
prime_list = []
for i in range(2, len(num_list)):
    if num_list[i]:
        prime_list.append(i)
        basis = i + i
        while (basis <= 1000000):
            num_list[basis] = 0
            basis = basis + i

num_list = [elem * elem for elem in prime_list]
for i in range(num_min, num_max + 1):
    for elem in num_list:
        if i % elem == 0:
            cnt += 1
print(num_max - num_min + 1 - cnt)
# print(prime_list[:5])