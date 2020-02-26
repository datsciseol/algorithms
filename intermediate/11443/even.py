def matrix_multiple(mat_a, mat_b):
    mat_c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mat_c[i][j] += mat_a[i][k] * mat_b[k][j] % 1000000007
            mat_c[i][j] = mat_c[i][j] % 1000000007
    return mat_c

def matrix_exponent(mat, num):
    ans = [[1, 0], [0, 1]]
    if num == 0:
        return ans
    elif num == 1:
        return mat
    else:
        while num > 0:
            if num % 2 == 1:
                ans = matrix_multiple(mat, ans)
            mat = matrix_multiple(mat, mat)
            num = num // 2
        return ans

basis = [[1, 1], [1, 0]]
num = int(input())
if num % 2:
    print((matrix_exponent(basis, num)[0][1] - 1) % 1000000007)
else:
    print((matrix_exponent(basis, num + 1)[0][1] - 1) % 1000000007)