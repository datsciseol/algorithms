num = int(input())
pack = num // 5
left = num % 5
while left > 0:
    if left % 3 == 0:
        pack += left // 3
        break
    pack -= 1
    left += 5
    if pack < 0:
        break
if pack < 0:
    print(-1)
else:
    print(pack)