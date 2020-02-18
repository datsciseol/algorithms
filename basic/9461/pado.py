result_list = [0] * 101
result_list[1] = 1
result_list[2] = 1
result_list[3] = 1
result_list[4] = 2
result_list[5] = 2
for num in range(6, 101):
    result_list[num] = result_list[num - 1] + result_list[num - 5]
test_case = int(input())
for _ in range(test_case):
    print(result_list[int(input())])