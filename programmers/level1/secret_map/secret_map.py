def sharp_change(a, b):
    ret = ""
    for elem in zip(a, b):
        c, d = elem
        if c == d:
            ret += c 
        else:
            ret += '1'
    return ret
def solution(n, arr1, arr2):
    def make_bin(num):
        base = bin(num)[2:].rjust(n, "0")
        return base
    new_arr1 = list(map(make_bin, arr1))
    new_arr2 = list(map(make_bin, arr2))
    output_list = [sharp_change(a, b) for a, b in zip(new_arr1, new_arr2)]
    answer = []
    for elem in output_list:
        answer.append(elem.replace("1", "#").replace("0", " "))
    return answer
n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
for elem in solution(n, arr1, arr2):
    print(elem)
