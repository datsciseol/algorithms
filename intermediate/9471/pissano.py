def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        result = fibonacci(num - 1) + fibonacci(num - 2)
        return result

num = int(input())
print(fibonacci(num))