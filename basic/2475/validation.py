num_list = list(map(int, input().split()))
result = 0
for elem in num_list:
    result += elem * elem
result = result % 10
print(result)
