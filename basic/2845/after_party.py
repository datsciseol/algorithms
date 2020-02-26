num, area = map(int, input().split())
people = num * area
news_list = map(int, input().split())
result_list = []
for elem in news_list:
    result_list.append(elem - people)
print(*result_list, sep = " ")