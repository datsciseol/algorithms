from collections import deque
import sys
input = sys.stdin.readline
dq1 = deque()
dq2 = deque()
string = input().rstrip()
dq1.extend(string)
order = int(input())
for _ in range(order):
    ord = input().rstrip()
    if ord[0] == 'L':
        if len(dq1):
            dq2.appendleft(dq1.pop())
    if ord[0] == "D":
        if len(dq2):
            dq1.append(dq2.popleft())
    if ord[0] == "B":
        if len(dq1):
            dq1.pop()
    if ord[0] == "P":
        p, char = ord.split()
        dq1.append(char)
dq1.extend(dq2)
print("".join(dq1))