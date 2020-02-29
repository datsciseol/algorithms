num_dict = {}
num_dict[1] = 1
num_dict[2] = 2
num_dict[3] = 4
for iter in range(4, 11):
    num_dict[iter] = (num_dict[iter - 1] + num_dict[iter - 2] + num_dict[iter - 3])
test_case = int(input())
for _ in range(test_case):
    print(num_dict[int(input())])