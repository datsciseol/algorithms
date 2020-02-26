time = int(input())
x = time // 5
y = time % 5
if y:
    y = 1
print(x + y)