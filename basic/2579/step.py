step = int(input())
step_list = [0]
for elem in range(step):
    step_list.append(int(input()))
dp_list = [0] * 301
dp_list[1] = step_list[1]
if step >= 2:
    dp_list[2] += (step_list[1] + step_list[2])
    if step >= 3:
        dp_list[3] = step_list[3] + max(step_list[1], step_list[2])
        for iter in range(4, step + 1):
            dp_list[iter] = max(step_list[iter] + dp_list[iter - 2], step_list[iter] + step_list[iter - 1] + dp_list[iter - 3])
print(dp_list[step])