test_num = int(input())


def average(arr):
    return (sum(arr[1:]) / arr[0])


for _ in range(test_num):
    over = 0
    num_list = list(map(int, input().split()))
    avg = average(num_list)
    for elem in num_list[1:]:
        if elem > avg:
            over += 1
    print("{:.3f}%".format(over/num_list[0] * 100))
