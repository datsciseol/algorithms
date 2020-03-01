def matrix_sum(A, B):
    C = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return C

A = [[1, 2, 3], [4, 5, 6]]
B = [[3, 4, 5], [5, 6, 7]]
print(matrix_sum(A, B))