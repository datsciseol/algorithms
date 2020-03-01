from collections import defaultdict
prime_dict = defaultdict(int)
prime_dict[1] = 1
prime_dict[2] = 0
for iter in range(2, 1000001):
    if prime_dict[iter] == 0:
        num = iter
        while num < 1000001:
            num += iter
            prime_dict[num] = 1
def solution(num):
    answer = 0
    for iter in range(2, num + 1):
        answer += (1 - prime_dict[iter])
    return answer

print(solution(int(input())))