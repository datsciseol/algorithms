def top(arr1):
    if len(arr1) == 0:
        return (-1)
    else:
        return (arr1[len(arr1) - 1])


num_stack = []
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output_list = []
scope = int(input())
for _ in range(scope):
    basis = int(input())
    while(1):
        if (top(num_stack) == basis):
            del num_stack[len(num_stack) - 1]
            output_list.append("-")
            break
        elif (top(num_stack) < basis):
            output_list.append("+")
            num_stack.append(num_list[0])
            del num_list[0]
        else:
            output_list.append("NO")
            break
if "NO" in output_list:
    print("NO")
else:
    for elem in output_list:
        print(elem)
