try:
    while True:
        n, k = map(int, input().split())
        coupon = n
        while n > 0:
            n = n // k
            coupon += n
            print(coupon) 
except:
    exit()