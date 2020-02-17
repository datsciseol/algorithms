num = int(input())
num_list = list(map(int, input().split()))

mum = int(input())
mum_list = list(map(int, input().split()))

for elem in mum_list:
    if (elem in num_list):
        print("1")
    else:
        print("0")