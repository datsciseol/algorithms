n, m = map(int, input().split())
num_dict = {}
num_dict[0] = 1
num_dict[1] = 1
num_dict[2] = 2
for iter in range(3, 101):
    num_dict[iter] = (iter) * num_dict[iter - 1]
print(num_dict[n] // (num_dict[m] * num_dict[n - m]))