num = int(input())
num_list = []
for _ in range(num):
    num_list.append(int(input()))
num_list.sort()
for elem in num_list:
    print(elem)