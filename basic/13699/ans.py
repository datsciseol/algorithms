ans_dict = {}
ans_dict[0] = 1
ans_dict[1] = 1
ans_dict[2] = 2
ans_dict[3] = 5
for iter in range(4, 36):
    ans_dict[iter] = 0
    for j in range(iter):
        ans_dict[iter] += ans_dict[j] * ans_dict[iter - 1 - j]
print(ans_dict[int(input())])