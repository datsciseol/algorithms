a, p = map(int, input().split())
answer_list = []
basis = a
b = 30
while b:
    b -= 1
    a = str(a)
    ans = 0
    for elem in a:
        ans += int(elem) ** p
    answer_list.append(ans)
    a = ans
print(answer_list)
print(set(answer_list))