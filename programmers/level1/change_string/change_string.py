def solution(s):
    minus = 1
    result = 0
    for elem in s:
        if elem == "-":
            minus = -1
        elif elem == "+":
            pass
        else:
            result = result * 10 + int(elem)
    return minus * result

print(solution(input()))
        