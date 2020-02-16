num = int(input())
num_list = list(map(int, input().split()))


def prime(num):
    i = 2
    if (num == 1):
        return (0)
    elif (num == 2):
        return (1)
    else:
        while (num / 2 >= i):
            if (num % i == 0):
                return (0)
            i = i + 1
        return (1)


cnt = 0
for elem in num_list:
    if prime(elem):
        cnt += 1
print(cnt)
