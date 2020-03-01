power_list = [elem ** 2 for elem in range(1, 320)]

def find_nearest(num, power_list):
    """find nearest powered integer which is smaller than num"""
    basis = power_list[0]
    ret = 1
    cnt = 0
    while basis <= num:
        ret = basis
        cnt += 1
        basis = power_list[cnt]
    return ret

num_input = int(input())
num_nearest = find_nearest(num_input, power_list)
dp_list = [0] * 639
dp_list[1] = 1
dp_list[2] = 2
dp_list[3] = 3
dp_list[4] = 1
for iter in range(5, 639):
    base = find_nearest(iter, power_list)
    if base == iter:
        dp_list[iter] = 1
    else:
        dp_list[iter] = dp_list[iter - base] + 1
print(1 + dp_list[num_input - num_nearest])