a = int(input())
b = int(input())
c = int(input())

num_array = []
for i in range(10):
    num_array.append(0)
result = str(a * b * c)
for elem in result:
    num_array[int(elem)] += 1
for elem in num_array:
    print(elem)
