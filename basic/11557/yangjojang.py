test_num = int(input())
for _ in range(test_num):
    school_num = int(input())
    school_dict = {}
    for _ in range(school_num):
        school, num = input().split()
        school_dict[school] = int(num)
    max_values = max(school_dict.values())
    for key, value in school_dict.items():
        if (value == max_values):
            print(key)
