from collections import deque
n, k = map(int, input().split())
people = deque(range(1, n + 1))
print("<", end = "")
people_list = []
while len(people):
    people.rotate(-(k - 1))
    people_list.append(people.popleft())
print(*people_list, sep = ", ", end = ">")
print()
