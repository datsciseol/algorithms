string = input().upper()
word_dict = {}
for elem in string:
    if elem not in word_dict:
        word_dict[elem] = 1
    word_dict[elem] += 1
cnt = 0
max_value = max(word_dict.values())
for key, value in word_dict.items():
    if (value == max_value):
        result = key
        cnt += 1
if (cnt > 1):
    print("?")
else:
    print(result)
