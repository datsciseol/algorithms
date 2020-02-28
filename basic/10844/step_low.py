num = int(input())
answer_list = [1] * 10
answer_list[0] = 0
temp_list = answer_list.copy()
for iter in range(num - 1):
    temp_list = [0] * 10
    temp_list[0] += answer_list[1] % 1000000000
    temp_list[1] += (answer_list[0] + answer_list[2]) % 1000000000
    temp_list[2] += (answer_list[1] + answer_list[3]) % 1000000000 
    temp_list[3] += (answer_list[2] + answer_list[4]) % 1000000000
    temp_list[4] += (answer_list[3] + answer_list[5]) % 1000000000
    temp_list[5] += (answer_list[4] + answer_list[6]) % 1000000000
    temp_list[6] += (answer_list[5] + answer_list[7]) % 1000000000
    temp_list[7] += (answer_list[6] + answer_list[8]) % 1000000000
    temp_list[8] += (answer_list[7] + answer_list[9]) % 1000000000
    temp_list[9] += answer_list[8] % 1000000000
    answer_list = temp_list.copy()
print(sum(answer_list) % 1000000000)