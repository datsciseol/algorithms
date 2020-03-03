n = int(input())
num_list = map(int, input().split())
div_list = [value / (idx + 1) for idx, value in enumerate(num_list)]
price = 0
while n > 0:
    print(div_list)
    print(n)
    max_num = max(div_list)
    max_idx = div_list.index(max_num)
    if n <= max_idx + 1:
        price += num_list[man_num]
        n -= (max_idx + 1)
        print(price)
    else:
        div_list.remove(max_num)
print(price)