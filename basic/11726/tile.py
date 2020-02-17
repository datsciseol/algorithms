result = [0] * 1001
num = int(input())
result[1] = 1
result[2] = 2
if num >= 3:
    for i in range(3, num + 1):
        result[i] = result[i - 1] + result[i - 2]
print(result[num] % 10007)
