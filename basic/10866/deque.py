import collections
import sys
input =sys.stdin.readline
class wow:
    def __init__(self):
        self.deque = collections.deque()
    def push_back(self, num):
        self.deque.append(num)
    def push_front(self, num):
        self.deque.appendleft(num)
    def front(self):
        if self.deque:
            return self.deque[0]
        else:
            return -1
    def pop_front(self):
        if self.deque:
            basis = self.deque[0]
            self.deque.popleft()
            return basis
        else:
            return -1
    def pop_back(self):
        if self.deque:
            basis = self.deque[-1]
            self.deque.pop()
            return basis
        else:
            return -1
    def back(self):
        if self.deque:
            return self.deque[-1]
        else:
            return -1
    def size(self):
        return len(self.deque)
    def empty(self):
        if self.deque:
            return 0
        else:
            return 1
result = wow()
case = int(input().rstrip('\n'))
for _ in range(case):
    oper = input().rstrip('\n')
    if " " in oper:
        oper, num = oper.split()
        num = int(num)

    if oper == "front":
        print(result.front())
    elif oper == "back":
        print(result.back())
    elif oper == "empty":
        print(result.empty())
    elif oper == "size":
        print(result.size())
    elif oper == "push_back":
        result.push_back(num)
    elif oper == "push_front":
        result.push_front(num)
    elif oper == "pop_front":
        print(result.pop_front())
    elif oper == "pop_back":
        print(result.pop_back())
