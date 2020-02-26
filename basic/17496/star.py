day, grow, cell, price = map(int, input().split())
if day % grow:
    took = day // grow
else:
    took = day // grow - 1
print(cell * price * (took))