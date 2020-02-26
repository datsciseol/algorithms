fibo_dict = {}
fibo_dict[0] = 0
fibo_dict[1] = 1
fibo_dict[2] = 1
for iter in range(3, 1000001):
    fibo_dict[iter] = (fibo_dict[iter - 1] + fibo_dict[iter - 2]) % 1000000000
num = int(input())
if num > 0:
    print(1)
    print(fibo_dict[num])
elif num < 0:
    if abs(num) % 2:
        print(1)
        print(fibo_dict[num * -1])
    else:
        print(-1)
        print(fibo_dict[num * -1])
else:
    print(0)
    print(0)