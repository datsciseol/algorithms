def floor_no(h, n):
    floor = n % h
    if floor == 0:
        floor += h
    return floor

def order_no(h, n):
    if n % h == 0:
        order = n // h
    elif n % h:
        order = n // h + 1
    return order

test_case = int(input())
for _ in range(test_case):
    h, w, n = map(int, input().split())
    room = ""
    floor = str(floor_no(h, n))
    order = str(order_no(h, n))
    if int(order) < 10:
        order = '0' + order
    room = floor + order
    print(room)