string = input()


def be_alpha(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for elem in alphabet:
        if elem not in string:
            print("-1", end=" ")
        else:
            print(string.index(elem), end=" ")


be_alpha(string)
