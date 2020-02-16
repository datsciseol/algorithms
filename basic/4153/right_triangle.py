while (1):
    num_list = list(map(int, input().split()))
    a, b, c = num_list
    if (not a and not b and not c):
        break
    c = max(num_list)
    num_list.remove(c)
    a, b = num_list
    if (c * c == a * a + b * b):
        print("right")
    else:
        print("wrong")
