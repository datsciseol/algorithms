def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []
    for idx, value in enumerate(answers):
        if pattern1[idx % 5] == value:
            score[0] += 1
        if pattern2[idx % 8] == value:
            score[1] += 1
        if pattern3[idx % 10] == value:
            score[2] += 1
    num_max = max(score)
    for iter in range(3):
        if score[iter] == num_max:
            answer.append(iter + 1)
    return answer

print(solution([1, 3, 2, 4, 2]))