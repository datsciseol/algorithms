e, s, m = map(int, input().split())

e_b = 0
s_b = 0
m_b = 0
basis = 0
while True:
    e_b = (e_b + 1) % 15
    s_b = (s_b + 1) % 28
    m_b = (m_b + 1) % 19
    basis += 1
    if e_b == 0:
        e_b += 15
    if s_b == 0:
        s_b += 28
    if m_b == 0:
        m_b += 19
    if e_b == e and m_b == m and s_b == s:
        break
print(basis)