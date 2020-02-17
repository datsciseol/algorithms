result = [0] * 91
result[0] = 0
result[1] = 1

num = int(input())
for i in range(2, num + 1):
    result[i] = result[i - 1] + result[i - 2]
print(result[num])
