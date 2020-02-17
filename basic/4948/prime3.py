import sys
input = sys.stdin.readline
def prime(num):
    if num == 0 or num == 1:
        return (0)
    elif num == 2:
        return (1)
    else:
        idx = 2
        while (idx <= num / 2):
            if (num % idx == 0):
                return (0)
            idx += 1
        return (1)
prime_list = [prime(elem) for elem in range(123456 * 2 + 1)]

def cnt_prime(num):
    cnt = 0
    dup = 2 * num
    basis = num + 1
    while (basis <= dup):
        if (prime_result[basis] == 1):
            cnt += 1
        basis += 1
    return (cnt)

while (True):
    num = int(input().rstrip('\n'))
    if num == 0:
        break
    print(cnt_prime(num))
