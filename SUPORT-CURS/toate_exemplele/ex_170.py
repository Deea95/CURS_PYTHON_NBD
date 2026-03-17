# 10.1.6 Ex. (170) – A function to load and display matrices
def load(c):
    n = c.split('|')
    m = []

    for i in range(len(n)):
        m.append(n[i].split(','))

    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m

def SMC(m):
    r = ""
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += str(m[i][j]) + ps(m[i][j],3)
        r += "\n"
    return r


def ps(a, s):
    t = ""
    b = s - (len(str(a)) % s)
    for i in range(b):
        t += " "
    return t


c1 = '12,2,44,1,0|34,5,6,7,8|' + \
     '1,2,3,4,5|5,4,3,2,1'
c2 = '66,5,45,10,10|37,50,60,17,18|' + \
     '10,25,37,4,5|5,4,3,2,1'
c3 = '66,5,45,10,10|37,50,60,17,18|' + \
     '10,25,37,4,5|5,4,3,2,1'
print(SMC(load(c1)))
print(SMC(load(c2)))
print(SMC(load(c3)))
