mod = 1000000007
fibo_dict = {}
def fibo(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif len(fibo_dict) > 0:
        return fibo_dict[num]
    else:
        if num % 2 == 1:
            m = (num + 1) // 2
            res1 = fibo(m)
            res2 = fibo(m - 1)
            fibo_dict[num] = res1 * res1 + res2 * res2
            fibo_dict[num] %= mod
            return fibo_dict[num]
        else:
            m = num // 2
            res1 = fibo(m - 1)
            res2 = fibo(m)
            fibo_dict[num] = (2 * res1 + res2) * res2
            fibo_dict[num] %= mod
            return fibo_dict[num]
n = int(input())
print(fibo(n))