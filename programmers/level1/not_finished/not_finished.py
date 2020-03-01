from collections import Counter
def solution(participant, completion):
    participate_counter = Counter(participant)
    complete_counter = Counter(completion)
    answer_dict = participate_counter - complete_counter
    answer = list(answer_dict)[0]
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))