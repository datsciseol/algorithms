num_list = []
for i in range(5):
    elem = int(input())
    if elem >= 40:
        num_list.append(elem)
    else:
        num_list.append(40)
print(sum(num_list)//5)
