def mat_multiple(mat_a, mat_b):
    mat_c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mat_c[i][j] += mat_a[i][k] * mat_b[k][j]
    return mat_c

def mat_exponent(mat, num):
    ans = [[1, 0], [0, 1]]
    if num == 0:
        return ans
    else:
        while num > 0:
            if num % 2:
                ans = mat_multiple(ans, mat)
            mat = mat_multiple(mat, mat)
            num = num // 2
        return ans
basis = [[1, 1], [1, 0]]
print(mat_exponent(basis, int(input()))[0][1])