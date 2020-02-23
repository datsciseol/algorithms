import sys
input = sys.stdin.readline
num = int(input().rstrip('\n'))
n_list = []
for _ in range(num):
    n_list.append(int(input().rstrip('\n')))
    
cnt = 1
basis = n_list[-1]
while n_list:
    if n_list[-1] > basis:
        cnt += 1
        basis = n_list[-1]
        n_list.pop()
    else:
        n_list.pop()
print(cnt)
