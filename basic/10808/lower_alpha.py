alphabet = "abcdefghijklmnopqrstuvwxyz"
string = input()
char_dict = {}
for char in alphabet:
    char_dict[char] = 0
for char in string:
    char_dict[char] += 1
for elem in char_dict.values():
    print(elem, end=" ")
