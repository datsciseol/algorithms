def solution(n, lost, reserve):
    lost_cleaned = [l for l in lost if l not in reserve]
    reserve_cleaned = [r for r in reserve if r not in lost]
    for elem in reserve_cleaned:
        left = elem - 1
        right = elem + 1
        if left in lost_cleaned:
            lost_cleaned.remove(left)
            continue
        if right in lost_cleaned:
            lost_cleaned.remove(right)
    return n - len(lost_cleaned)

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
print(solution(n, lost, reserve))