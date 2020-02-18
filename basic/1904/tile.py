num_list = [0] * 1000001

num_list[0] = 1
num_list[1] = 1
num_list[2] = 2
num_list[3] = 3
num_list[4] = 5
for i in range(5, 1000001):
    num_list[i] = (num_list[i - 1] + num_list[i - 1]) % 15746
print(num_list[int(input())])