length = int(input())
word_list = []
for _ in range(length):
    word_list.append(input())
word_list = list(set(word_list))
word_list.sort(key = lambda x : (len(x), x))
for elem in word_list:
    print(elem)