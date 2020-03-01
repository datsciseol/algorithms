def solution(arr, divisor):
    return sorted([elem for elem in arr if elem % divisor == 0]) or [-1]

arr = [5, 8, 7, 10]
divisor = 5
print(solution(arr, divisor))