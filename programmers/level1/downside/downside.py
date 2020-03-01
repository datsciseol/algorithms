def solution(s):
    lower_list = []
    upper_list = []
    for elem in s:
        if elem.islower():
            lower_list.append(elem)
        else:
            upper_list.append(elem)
    lower_list.sort(reverse = True)
    upper_list.sort(reverse = True)
    result = (lower_list + upper_list)
    answer = "".join(result)
    return result
