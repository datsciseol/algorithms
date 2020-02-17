x, y, w, h = map(int, input().split())
num_list = []
num_list.append(x)
num_list.append(w - x)
num_list.append(y)
num_list.append(h - y)
num_min = min(num_list)
print(num_min)
