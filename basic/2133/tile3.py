result = [0] * 31
result[0] = 1
result[1] = 0
result[2] = 3
result[3] = 0
result[4] = 11
for num in range(5, 31):
    if (num % 2 == 1):
        result[num] = 0
    else:
        i = num
        result[num] += result[num - 2]
        while (i > 0):
            result[num] += 2 * result[i - 2]
            i = i - 2
print(result[int(input())])
