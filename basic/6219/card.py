from collections import deque

result_list = [elem for elem in range(1, int(input()) + 1)]
result = deque()
result.extend(result_list)
while len(result) > 1:
    result.popleft()
    result.rotate(-1)
print(result[0])