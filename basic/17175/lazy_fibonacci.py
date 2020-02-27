answer_dict = {}
answer_dict[0] = 1
answer_dict[1] = 1
answer_dict[2] = 3
for iter in range(3, 51):
    answer_dict[iter] = (answer_dict[iter - 1] + answer_dict[iter - 2] + 1) % 1000000007
print(answer_dict[int(input())])
