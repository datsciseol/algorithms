def solution(a, b):
    answer = ""
    day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_dict = {}
    day_dict[1] = 31
    for iter in range(2, 13):
        day_dict[iter] = day_dict[iter - 1] + day_list[iter - 1]
    day = 0
    for elem in range(1, a):
        day += day_dict[elem]
    day += b
    day7_dict = {1 : "FRI", 2 : "SAT", 3 : "SUN", 4 : "MON", 5 : "TUE", 6 : "WED", 0 : "THU"}
    answer = day7_dict[day % 7]
    return answer
print(solution(5, 24))