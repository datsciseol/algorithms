test_num = int(input())
num_stack = []
for _ in range(test_num):
    basis = int(input())
    if basis == 0:
        num_stack.pop()
    else:
        num_stack.append(basis)
print(sum(num_stack))