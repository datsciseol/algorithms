def matrix_multiple(mat_a, mat_b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += ((mat_a[i][k] * mat_b[k][j]) % 1000000000)
    return result 

def matrix_exp(basis, num):
    ans = [[1, 0], [0, 1]]
    if num == 0:
        return ans
    elif num == 1:
        return basis
    else:
        while num > 0:
            if num % 2 == 1:
                ans = matrix_multiple(ans, basis)
            basis = matrix_multiple(basis, basis)
            num = num // 2
        return ans
basis = [[1, 1], [1, 0]]

a, b = map(int, input().split())
a %= 1500000000
b %= 1500000000
result = matrix_exp(basis, b + 2)[0][1] - matrix_exp(basis, a + 1)[0][1]
if result < 0:
    result += 1000000000
result %= 1000000000
print(result)