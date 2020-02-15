def hansu(num):
    num = str(num)
    len_num = len(num)
    if (len_num <= 2):
        return (1)
    for i in range(len_num - 2):
        if ((int(num[i]) - int(num[i + 1])) != (int(num[i + 1]) - int(num[i + 2]))):
            return (0)
    return (1)


result = 0
scope = int(input())
for i in range(1, scope + 1):
    result += hansu(i)
print(result)
