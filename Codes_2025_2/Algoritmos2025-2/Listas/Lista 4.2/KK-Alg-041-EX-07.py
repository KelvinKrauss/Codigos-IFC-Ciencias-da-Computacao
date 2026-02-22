m1 = 2
m2 = 3
m3 = 4
a = 0
mm1 = 4
mm2 = 5
mm3 = 6
pi = 3
print(pi)
while a < 7:
    a = a + 1 
    pi = pi + 4 / (m1 * m2 * m3)
    print(pi)
    pi = pi - 4 / (mm1 * mm2 * mm3)
    m1 = m1 + 4
    m2 = m2 + 4
    m3 = m3 + 4
    mm1 = mm1 + 4
    mm2 = mm2 + 4
    mm3 = mm3 + 4
    print(pi)