while True:
    string = input()
    if string == ".":
        break
    else:
        ps_stack = []
        for char in string:
            if char in "([":
                ps_stack.append(char)
            elif char == "]":
                try:
                    if ps_stack[-1] == "[":
                        ps_stack.pop()
                    else:
                        print("no")
                        break
                except:
                    print("no")
                    break
            elif char == ")":
                try:
                    if ps_stack[-1] == "(":
                        ps_stack.pop()
                    else:
                        print("no")
                        break
                except:
                    print("no")
                    break
        else:
            if len(ps_stack):
                print("no")
            else:
                print("yes")