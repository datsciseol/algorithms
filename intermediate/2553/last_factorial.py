from collections import defaultdict
num_dict = defaultdict(int)
num_dict[0] = 1
num_dict[1] = 1
for iter in range(2, 20001):
    num_dict[iter] = (iter * num_dict[iter - 1])
    if num_dict[iter] % 10 == 0:
        num_dict[iter] = num_dict[iter] // 10
    else:
        num_dict[iter] = num_dict[iter] % 1000000000

num_input = num_dict[int(input())]
while num_input % 10 == 0:
    num_input = num_input // 10
print(num_input % 10)


 
