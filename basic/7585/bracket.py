while True:
    string = input()
    if string == "#":
        break
    else:
        vps_stack = []
        for elem in string:
            if elem in "([{":
                vps_stack.append(elem)
            else:
                if elem in ")]}":
                    try:
                        if elem == ")":
                            if vps_stack[-1] == "(":
                                vps_stack.pop()
                            else:
                                print("Illegal")
                                break
                        elif elem == "]":
                            if vps_stack[-1] == "[":
                                vps_stack.pop()
                            else:
                                print("Illegal")
                                break
                        elif elem == "}":
                            if vps_stack[-1] == "{":
                                vps_stack.pop()
                            else:
                                print("Illegal")
                                break
                    except:
                        print("Illegal")
                        break
        else:
            if len(vps_stack):
                print("Illegal")
            else:
                print("Legal")