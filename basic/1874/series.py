import sys
input = sys.stdin.readline
scope = int(input().rstrip('\n'))
n_stack = []
output_list = []
num_list = []


def topp(arr):
    if not arr:
        return -1
    else:
        return arr[-1]


num_list = [elem for elem in range(1, scope + 1)]
for _ in range(scope):
    basis = int(input().rstrip('\n'))
    while True:
        top = topp(n_stack)
        num_len = len(n_stack)
        if (basis > top and num_list[0]):
            n_stack.append(num_list[0])
            output_list.append("+")
            del num_list[0]
        elif (basis == top and n_stack[0]):
            del n_stack[num_len - 1]
            output_list.append('-')
            break
        else:
            output_list.append("NO")
            break
if "NO" in output_list:
    print("NO")
    sys.exit()
else:
    for elem in output_list:
        print(elem)
