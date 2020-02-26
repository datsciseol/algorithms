n, m = map(int, input().split())
def find_five(num):
    result = 0
    while num:
        num = num // 5
        result += num
    return result

def find_two(num):
    result = 0
    while num:
        num = num // 2
        result += num
    return result

n_five, n_two = find_five(n), find_two(n)
m_five, m_two = find_five(m), find_two(m)
nm_five, nm_two = find_five(n - m), find_two(n - m)
result_five = n_five - m_five - nm_five
result_two = n_two - m_two - nm_two

if result_five >= result_two:
    print(result_two)
else:
    print(result_five)

