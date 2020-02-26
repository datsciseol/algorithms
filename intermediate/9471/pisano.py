def pisano(num):
    limit = num ** 2 - 1
    period_list = [0, 1]
    fibonacci_dict = {}
    fibonacci_dict[0] = 0
    fibonacci_dict[1] = 1
    for iter in range(2, limit):
        period_list.append((fibonacci_dict[iter - 1] + fibonacci_dict[iter - 1]) % num)
    return period_list
print(pisano(6))