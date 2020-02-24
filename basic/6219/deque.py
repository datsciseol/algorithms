from collections import deque

thing = deque()
thing.append(3)
thing.appendleft(2)
thing.extend([1, 2, 3, 4])
for _ in range(3):
    thing.rotate(1)
    print(thing)