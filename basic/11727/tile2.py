num_dict = {}
num_dict[1] = 1
num_dict[2] = 3
for iter in range(3, 1001):
    num_dict[iter] = (2 * num_dict[iter - 2] + num_dict[iter - 1]) % 10007
print((num_dict[int(input())]) % 10007)