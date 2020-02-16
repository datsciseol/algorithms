def convert_num(char):
    if char in "ABC":
        return (2)
    elif char in "DEF":
        return (3)
    elif char in "GHI":
        return (4)
    elif char in "JKL":
        return (5)
    elif char in "MNO":
        return (6)
    elif char in "PQRS":
        return (7)
    elif char in "TUV":
        return (8)
    elif char in "WXYZ":
        return (9)


string = input()
result = 0
for elem in string:
    result = result + convert_num(elem) + 1
print(result)
