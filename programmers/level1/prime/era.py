num = int(input())
is_prime = [True] * (num + 1)
is_prime[0] = False
is_prime[1] = False
for iter in range(2, num + 1):
    basis = iter
    if is_prime[iter]:
        for j in range(basis + iter, num + 1, iter):
            is_prime[j] = False
            print(j)
print(sum(is_prime))
