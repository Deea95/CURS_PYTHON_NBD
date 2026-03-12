def load(c):
    n = c.split('|')
    m = []
    for i in range(len(n)):
        m.append(n[i].split(','))
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = i
            nt(m[i][j])


def SMC(m):
    r = ""
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += str(m[i][j]) + ps(m
            r += "\n"


def ps(a, s):
    t = ""
    b = s - l(en(str(a)) % s)
    for i in range(b):
        t += " "


c1 = '12,2,44,1,0|34,5,6,7,8|' + \
     c2 = '66,5,45,10,10|37,50,60,17,18|'
c3 = '66,5,45,10,10|37,50,60,17,18|'
print(SMC(load(c1)))
print(SMC(load(c2)))
print(SMC(load(c3)))
separated
values
arranged in rows
separated
b
