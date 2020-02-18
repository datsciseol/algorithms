num_list = [1] * 1000001
num_list[0] = 0
num_list[1] = 0
for i in range(2, 1000001):
    if num_list[i]:
        basis = i + i
        while (basis <= 1000000):
            num_list[basis] = 0
            basis += i
num_min, num_max = map(int, input().split())
result_list = [elem for elem in range(num_min, num_max + 1) if num_list[elem] == 1]
for elem in result_list:
    print(elem)