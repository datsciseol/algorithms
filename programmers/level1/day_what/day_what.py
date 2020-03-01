def solution(a, b):
    day_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for iter in range(a):
        day += day_list[iter]
    day += b
    week = {0 : "THU", 1 : "FRI", 2 : "SAT", 3 : "SUN", 4: "MON", 5 : "TUE", 6 : "WED"}
    answer = week[day % 7]
    return answer
a, b = map(int, input().split())
print(solution(a, b))