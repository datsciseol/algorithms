test_num = int(input())

for _ in range(test_num):
    yonsei = 0
    korea = 0
    for _ in range(9):
        y, k = map(int, input().split())
        yonsei += y
        korea += k
    if (yonsei > korea):
        print("Yonsei")
    elif (yonsei < korea):
        print("Korea")
    else:
        print("Draw")
