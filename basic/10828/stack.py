
opers = int(input().rstrip('\n'))
stack = []

for i in range(opers):
    cmd = input().rstrip('\n')
    if (cmd == "empty"):
        print(int(len(stack) == 0))
    elif (cmd == "size"):
        print(len(stack))
    elif (cmd == "top"):
        if (len(stack) == 0):
            print("-1")
        else:
            print(stack[len(stack) - 1])
    elif (cmd.split()[0] == "push"):
        stack.append(int(cmd.split()[1]))
    elif (cmd == "pop"):
        if (len(stack)):
            print(stack[len(stack) - 1])
            del stack[len(stack) - 1]

        else:
            print("-1")
