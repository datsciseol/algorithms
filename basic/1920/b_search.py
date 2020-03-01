def search(elem, num_list):

    def b_search(elem, num_list, start, end):
        if start == end:
            return num_list[start] == elem
        else:
            mid = (start + end) // 2
            if num_list[mid] == elem:
                return True
            elif num_list[mid] < elem:
                if start == mid:
                    return False
                else:
                    start = mid + 1
                    return b_search(elem, num_list, start, end)
            else: # num_list[mid] < elem
                return b_search(elem, num_list, start, mid - 1)
    if len(num_list) == 0:
        return False
    else:
        return b_search(elem, num_list, 0, len(num_list) - 1)
print(search(1.5, [1, 2, 3, 4]))