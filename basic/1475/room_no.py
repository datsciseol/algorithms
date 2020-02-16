from collections import defaultdict
import math
num = list(input())
num_dict = defaultdict(int)
result_dict = defaultdict(int)
for elem in num:
    num_dict[elem] += 1
for k, v in num_dict.items():
    if (k == "6" or k == "9"):
        result_dict["thing"] += v
    else:
        result_dict[k] += v
result_dict["thing"] = math.ceil(result_dict["thing"] / 2)
max_num = max(result_dict.values())
print(max_num)
