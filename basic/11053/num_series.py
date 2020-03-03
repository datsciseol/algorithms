num = int(input())
num_list = list(map(int, input().split()))
num_list = [0] + num_list
dp_list = [0] * (num + 1)
dp_list[1] = 1
for iter in range(2, num + 1):
    output_list = []
    for jter in range(iter):
        if num_list[iter] > num_list[jter]:
            output_list.append((dp_list[jter], jter))
    output_list.sort(reverse = True, key = lambda x : x[0])
    max_idx = output_list[0][1]
    dp_list[iter] = dp_list[max_idx] + 1
print(max(dp_list))