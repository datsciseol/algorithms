def solution(n, m):
    x , y = max(n, m), min(n, m)
    basis = 1
    while basis > 0:
        basis = x % y
        x, y = y, basis
    answer = [x, int(n * m / x)]
    return answer
print(solution(3, 2))