num = int(input())
divid = 1
basis = num + 9
result = 1
while num > 0:
    result = result * basis
    divid *= num
    basis -= 1
    num -= 1
print((result//divid) % 10007)
