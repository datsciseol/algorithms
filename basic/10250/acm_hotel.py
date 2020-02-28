test_case = int(input())
for _ in range(test_case):
    height, width, nth = map(int, input().split())
    y = nth % height
    if y == 0:
        y += height
        y = str(y)
    else:
        y = str(y)
    if nth //height == 1:
        x = nth // height
    else:
        x = nth // height + 1
    if x < 10:
        x = '0' + str(x)
    else:
        x = str(x)
    result = y + x
    print(result)

