m1, m2, m3 = input().split()
# if 93<m1<728 and 93<m2<728 and 93<m3<728:
m1 = int(m1)
m2 = int(m2)
m3 = int(m3)
m_max = m1
m_min = m1

if m2 > m_max:
    m_max = m2
if m3 > m_max:
    m_max = m3
if m2 < m_min:
    m_min = m2
if m3 < m_min:
    m_min = m3

if m_min >= 94 and m_max <= 727:
    print(m_max)
else:
    print("Error")