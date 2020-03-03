from collections import Counter
from collections import defaultdict
num = int(input())
num_dict = Counter(map(int, input().split()))
num2 = int(input())
check_list = map(int, input().split())
for elem in check_list:
    if elem in num_dict.keys():
        print(num_dict[elem], end = " ")
    else:
        print(0, end = " ")
print()
