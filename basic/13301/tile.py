a = [1] * 81
a[0] = 0
for i in range(2, 81):
    a[i] = a[i - 1] + a[i - 2]

b = [1] * 81
b[0] = 0
b[1] = 4
b[2] = 6
for i in range(3, 81):
    b[i] = 4 * a[i] + 2 * a[i - 1]

num = int(input())
print(b[num])