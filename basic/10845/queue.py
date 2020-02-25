from collections import deque
import sys
input =sys.stdin.readline
queue = deque()
opers = int(input().rstrip('\n'))

def dopop(queue):
    if queue:
        result = queue[0]
        queue.popleft()
        return result
    else:
        return -1

def is_empty(queue):
    if queue:
        return 0
    else:
        return 1

def front(queue):
    if queue:
        return queue[0]
    else:
        return -1

def back(queue):
    if queue:
        return queue[-1]
    else:
        return -1

for _ in range(opers):
    calc = input().rstrip('\n')
    if calc[:4] == "push":
        num = int(calc.split()[1])
        queue.append(num)
    elif calc == "pop":
        print(dopop(queue))
    elif calc == "front":
        print(front(queue))
    elif calc == "back":
        print(back(queue))
    elif calc == "empty":
        print(int(len(queue) == 0))
    elif calc == "size":
        print(len(queue))