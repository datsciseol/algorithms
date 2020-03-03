num_dict = {'0' : '000', '1' : '001', '2' : '010', '3' : '011' , '4' : '100', '5' : '101', '6' : '110', '7' : '111'}
num = input()
ret = ""
for elem in num:
    ret = ret + num_dict[elem]
if ret[0] == '0':
    if ret[1] == '0':
        ret = ret[2:]
    else:
        ret = ret[1:]
print(ret)