test_num = int(input())
num_dict = {}
for _ in range(test_num):
    age, name = input().split()
    num_dict[name] = age
print(num_dict)
