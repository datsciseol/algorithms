def solution(n):
    base = n ** (0.5)
    if base % 1 == 0:
        return (base + 1) ** 2
    return -1