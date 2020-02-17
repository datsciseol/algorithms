def opers(char, num_list):
    if char == "R":
        num_list = num_list[::-1]
        print(num_list)
        return (1)
    elif char == "D":
        if not num_list:
            return (0)
        else:
            del num_list[0]
            print(num_list)
            return (1)


test_case = int(input())
for _ in range(test_case):
    func = input()
    num = int(input())
    string = input()
    string = string.replace("[", "").replace("]", "")
    for oper in func:
        if not opers(oper, string):
            print("error")
            break
    print(string)
