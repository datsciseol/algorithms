fibonacci_dict = {}
fibonacci_dict[0] = 0
fibonacci_dict[1] = 1
fibonacci_dict[2] = 1
for iter in range(3, 1500001):
    fibonacci_dict[iter] = (fibonacci_dict[iter - 1] + fibonacci_dict[iter - 2]) % 1000000
num = int(input())
num = num % 1500000
print(fibonacci_dict[num])

# matrix multiplication
