num = input()
basis = 0
ret = int(num)
while ret > 9:
    ret = 0
    for elem in num:
        ret += int(elem)
    basis += 1
    num = str(ret)

print(basis)

if ret in [3, 6, 9]:
    print("YES")
else:
    print("NO")