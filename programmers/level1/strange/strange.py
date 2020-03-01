def solution(s):
    word_list = s.split(" ")
    new_word_list = []
    for word in word_list:
        new_word = ""
        for iter in range(len(word)):
            if iter % 2 == 0:
                new_word += word[iter].upper()
            else:
                new_word += word[iter].lower()
        new_word_list.append(new_word)
    print(new_word_list)
    answer = " ".join(new_word_list)
    return answer
s = "ilo     i got"
print(solution(s))