test_case = int(input())
for _ in range(test_case):
    num_list = list(map(int, input().split()))
    result_list = [elem for elem in num_list if elem % 2 == 0]
    result_list.sort()
    print(sum(result_list), result_list[0])