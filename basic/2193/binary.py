dp_list = [[0, 0] for elem in range(91)]
dp_list[0][0] = 0
dp_list[0][1] = 0
dp_list[1][0] = 0
dp_list[1][1] = 1
dp_list[2][0] = 1
dp_list[2][1] = 0
for iter in range(3, 91):
    dp_list[iter][0] = dp_list[iter - 1][0] + dp_list[iter - 1][1]
    dp_list[iter][1] = dp_list[iter - 1][0]
num = int(input())
print(sum(dp_list[num]))