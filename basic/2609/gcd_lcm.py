def gcd(a, b):
    i = 1
    gcd_list = []
    while (i <= a and i <= b):
        if (a % i == 0 and b % i == 0):
            gcd_list.append(i)
        i += 1
    return (max(gcd_list))


a, b = map(int, input().split())
num_gcd = gcd(a, b)
num_lcm = int(a * b / num_gcd)
print(num_gcd)
print(num_lcm)
