n_list = []
num = int(input())
for _ in range(num):
    n_list.append(int(input()))
basis = n_list[len(n_list) - 1]
cnt = 1
while n_list:
    if n_list[len(n_list) - 1] > basis:
        cnt += 1
        basis = n_list[len(n_list) - 1]
        del n_list[len(n_list) - 1]
    else:
        del n_list[len(n_list) - 1]
print(cnt)