num_list = []

for i in range(9):
    num_list.append(int(input()))
max_input = max(num_list)
print(max_input)
print(num_list.index(max_input) + 1)
