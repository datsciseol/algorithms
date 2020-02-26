time_list = []
for _ in range(4):
    time_list.append(int(input()))
time = sum(time_list)
x = time // 60
y = time % 60
print(x)
print(y)