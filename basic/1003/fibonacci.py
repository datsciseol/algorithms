test_case = int(input())
zero_list = [0] * 41
one_list = [0] * 41

zero_list[0] = 1
zero_list[1] = 0
zero_list[2] = 1
zero_list[3] = 1
for i in range(3, 41):
    zero_list[i] = zero_list[i - 1] + zero_list[i - 2]

one_list[0] = 0
one_list[1] = 1
one_list[2] = 1
one_list[3] = 2
for i in range(3, 41):
    one_list[i] = one_list[i - 1] + one_list[i - 2]

for _ in range(test_case):
    num = int(input())
    print(zero_list[num], one_list[num])