num_list = [1] * (123456 *2 + 1)
num_list[0] = 0
num_list[1] = 0
for i in range(2, (123456 * 2 + 1)):
    if num_list[i]:
        basis = i + i
        while (basis <= (123456 * 2)):
            num_list[basis] = 0
            basis += i
while (1):
    num = int(input())
    if num == 0:
        break
    cnt = 0
    for i in range(num + 1, 2 * num + 1):
        if num_list[i] == 1:
            cnt += 1
    print(cnt)    
