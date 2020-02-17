num = int(input())
result = [0] * 10001
result[0] = 0
result[1] = 1
result[2] = 1

for i in range(2, 10001):
    result[i] = result[i - 1] + result[i - 2]
print(result[num])
