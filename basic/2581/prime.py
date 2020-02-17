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

num_min = int(input())
num_max = int(input())
num_list = [elem for elem in range(num_min, num_max + 1) if prime(elem) == 1]
if (len(num_list) == 0):
    print("-1")
else:
    print(sum(num_list))
    print(num_list[0])