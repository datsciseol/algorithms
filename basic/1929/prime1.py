def prime(num):
    if num == 0 or num == 1:
        return (0)
    elif num == 2:
        return (1)
    else:
        basis = 2
        while (basis <= num / 2):
            if (num % basis == 0):
                return (0)
            basis += 1
        return (1)
num_min ,num_max = map(int, input().split())
num_list = [elem for elem in range(num_min, num_max + 1) if prime(elem) == 1]
for elem in num_list:
    print(elem)