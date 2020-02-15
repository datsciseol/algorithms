def self_num(num):
    result = num
    num = str(num)
    for elem in num:
        result += int(elem)
    return result


check_num = [1] * 10000
basis = 1
while (basis < 10000):
    if (check_num[basis] == 0):
        basis += 1
        continue
    num = basis
    while (self_num(num) <= 9999):
        num = self_num(num)
        check_num[num] = 0
    basis += 1
check_num[0] = 0
for i in range(len(check_num)):
    if check_num[i] == 1:
        print(i)
