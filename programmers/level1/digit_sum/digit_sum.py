def digit_sum(num):
    if num < 10:
        return num
    else:
        return num % 10 + digit_sum(num // 10)

print(digit_sum(123))