import sys
import collections
input = sys.stdin.readline
test_case = int(input().rstrip())
for i in range(test_case):
    opers = input().rstrip()
    length = int(input().rstrip())
    num_list = input().rstrip()[1:-1].split(',')
    reverse = 0
    if length != 0:
        try:
            for oper in opers:
                if oper == "R":
                    reverse += 1
                elif oper == "D" and reverse % 2 == 0:
                    del num_list[0]
                    
                elif oper == "D" and reverse % 2 == 1:
                    num_list.pop()
            if reverse % 2:
                num_list = num_list[::-1]
                print("[", end = "")
                print(*num_list, sep = ",", end = "")
                print("]")
                
            else:
                print("[", end = "")
                print(*num_list, sep = ",", end = "")
                print("]")

        except:
            print("error")
    else:
        for oper in opers:
            if oper == "D":
                print("error")
                break
        else:
            print("[]")
