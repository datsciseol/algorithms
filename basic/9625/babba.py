num = int(input())

a_list = [1] * 46
a_list[0] = 0
a_list[1] = 0
a_list[2] = 1
for i in range(3, 46):
    a_list[i] = a_list[i - 1] + a_list[i - 2]

b_list = [1] * 46
b_list[0] = 0
b_list[1] = 1
b_list[2] = 1
for i in range(2, 46):
    b_list[i] = b_list[i - 1] + b_list[i - 2]

print(a_list[num], b_list[num])