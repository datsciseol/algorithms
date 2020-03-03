from collections import defaultdict
try:
    num_dict = defaultdict(int)
    num_dict[0] = 1
    num_input = input()
    if int(num_input[0]) >= 1 and int(num_input[0]) <= 9:
        num_dict[1] = 1
    length = len(num_input)
    if length >= 2:
        if int(num_input[1]) >= 1 and int(num_input[1]) <= 9:
            num_dict[2] = 1
        if int(num_input[0] + num_input[1]) >= 10 and int(num_input[0] + num_input[1]) <= 26:
            num_dict[2] += 1
        for iter in range(3, length + 1):
            if int(num_input[iter - 1]) >= 1 and int(num_input[iter - 1]) <= 9:
                num_dict[iter] = num_dict[iter - 1]
            if int(num_input[iter - 2] + num_input[iter - 1]) >= 10 and int(num_input[iter - 2] + num_input[iter - 1]) <= 26:
                num_dict[iter] += num_dict[iter - 2]
    if num_input[0] == '0':
        print(0)
    else:
        print(num_dict[length] % 1000000)
        
except:
    print(0)