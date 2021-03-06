def search(elem, num_list):
    def b_search(elem, num_list, start, end):
        if start == end:
            return int(num_list[start] == elem)
        mid = (start + end) // 2
        if num_list[mid] == elem:
            return 1
        elif num_list[mid] > elem:
            if start == mid:
                return 0
            else:
                return b_search(elem, num_list, start, mid - 1)
        else:
            return b_search(elem, num_list, mid + 1, end)
    if len(num_list) == 0:
        return 0
    else:
        return b_search(elem, num_list, 0, len(num_list) - 1)
    
num = input()
num_list = list(map(int, input().split()))
num_list.sort()
length = input()
check_list = map(int, input().split())
for elem in check_list:
    print(search(elem, num_list))