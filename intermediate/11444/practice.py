num = 13
ans = 1
mat = 2
while num > 0:
    if num % 2 == 1:
        ans = mat * ans
    mat = mat * mat
    num /= 2
print(ans)