import sys
input = sys.stdin.readline

prime_list = [True] * (123456 * 2 + 1)
prime_list[0] = False
prime_list[1] = False
idx = 2
while (idx <= (123456 * 2 + 1)):
    if prime_list[idx]:
        for i in range(idx + idx, 123456 * 2 + 1, idx):
            prime_list[i] = False
    idx += 1
print(prime_list)






# def cnt_prime(num):
#     cnt = 0
#     dup = 2 * num
#     basis = num + 1
#     while (basis <= dup):
#         if (prime_result[basis] == 1):
#             cnt += 1
#         basis += 1
#     return (cnt)

# while (True):
#     num = int(input().rstrip('\n'))
#     if num == 0:
#         break
#     print(cnt_prime(num))
