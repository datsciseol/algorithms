test_num = int(input())

for _ in range(test_num):
    p_stack = []
    sum = 0
    ps = input()
    for char in ps:
        if char == "(":
            p_stack.append("(")
            sum += 1
        elif char == ")":
            if p_stack:
                sum -= 1
                p_stack.pop()
            else:
                sum -= 50
                break
    if (sum == 0):
        print("YES")
    else:
        print("NO")
