import sys
from collections import defaultdict
input = sys.stdin.readline
num = int(input())
if num % 3 == 0:
    result = "YES"
else:
    result = "NO"

num_list = defaultdict(int)
for i in range(10):
    num_list[i] = 0
    
for iter in range(10, 55):
    basis = str(iter)
    num_sum = sum(map(int, basis))
    num_list[iter] = num_list[num_sum] + 1

if num >= 55:
    ret = sum(map(int, str(num)))
    print(num_list[ret] + 1)
    print(result)
else:
    print(num_list[num])
    print(result)
    