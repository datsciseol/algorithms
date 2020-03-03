numbers = [6, 10, 2]
def solution(numbers):
    length = len(numbers)
    check_list = [False] * length
    answer = []
    answer_list = []
    def depth_fs(numbers, num):
        if num == length:
            answer_list.append(int("".join(answer)))
        for iter in range(length):
            if check_list[iter]:
                continue
            check_list[iter] = True
            answer.append(str(numbers[iter]))
            depth_fs(numbers, num + 1)
            answer.pop()
            check_list[iter] = False
    depth_fs(numbers, 0)
    answer_list.sort(reverse = True)
    ret = answer_list[0]
    return ret
print(solution(numbers))