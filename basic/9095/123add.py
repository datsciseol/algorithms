test_case = int(input())
num_arr = [0] * 12
num_arr[1] = 1
num_arr[2] = 2
num_arr[3] = 4
for i in range(4, 12):
    num_arr[i] = num_arr[i - 1] + num_arr[i - 2] + num_arr[i - 3]
for _ in range(test_case):
    print(num_arr[int(input())])
