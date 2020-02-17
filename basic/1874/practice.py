stack = []
output_list = []

k = 1
scope = int(input())
for _ in range(scope):
    basis = int(input())
    while (k < basis):
        stack.append(k)
        output_list.append("+")
        k += 1
    if (k == basis):
        stack.pop()
        output_list.append('-')
if not len(stack):
    for i in output_list:
        print(i)
else:
    print("NO")
