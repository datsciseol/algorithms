sent_num = int(input())

for _ in range(sent_num):
    sent = input().split()
    for word in sent:
        print(word[::-1], end=" ")
