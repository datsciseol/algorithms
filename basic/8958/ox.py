test_num = int(input())


def count_num(string):
    point = 0
    for i in range(len(string)):
        point += (i + 1)
    return (point)


for _ in range(test_num):
    point = 0
    ox = list(input().split("X"))
    for elem in ox:
        point += count_num(elem)
    print(point)
