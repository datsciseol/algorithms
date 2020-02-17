card_num = int(input())
num_str = ""
for i in range(card_num):
    num_str += str(i + 1)
num_str = list(num_str)
while (len(num_str) > 1):
    del num_str[0]
    basis = num_str[0]
    del num_str[0]
    num_str = num_str.append(basis)
print(num_str)
