num_list = [0]
for elem in range(1, 1001):
    cnt = 0
    while (cnt < elem):
        cnt += 1
        num_list.append(elem)
a, b = map(int, input().split())
print(sum(num_list[a : b + 1]))