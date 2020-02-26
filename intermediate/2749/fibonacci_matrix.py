def matrix_multiple(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += (a[i][k] * b[k][j] % 1000000)
    return c

def exp(basis, num):
    if num == 1:
        return basis
    elif num % 2 == 0:
        result = matrix_multiple(exp(basis, num //2), exp(basis, num//2))
        return result
    else:
        result = matrix_multiple(basis, matrix_multiple(exp(basis, num // 2), exp(basis, num // 2))) 
        return result
basis = [[1, 1], [1, 0]]



num = int(input()) % 1500000
print(exp(basis, num)[0][1] % 1000000)
