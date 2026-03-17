# 10.1.6 Ex. (170) – A function to load and display matrices
def load(c):                      Output:


n = c.split('|')
m = []
12
2
44
1
0
for i in range(len(n)):         1
2
3
4
5
m.append(n[i].split(','))
5
4
3
2
1
for i in range(len(m)):         66
5
45
10
10
for j in range(len(m[i])):    37
50
60
17
18
m[i][j] = i
nt(m[i][j])
return m


def SMC(m):
    r = ""
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += str(m[i][j]) + ps(m[i][j], 3)
        r += "\n"
    return r


def ps(a, s):
    t = ""
    b = s - l(en(str(a)) % s)
    for i in range(b):
        t += " "
    return t


c1 = '12,2,44,1,0|34,5,6,7,8|' + \
     c2 = '66,5,45,10,10|37,50,60,17,18|' + \
          c3 = '66,5,45,10,10|37,50,60,17,18|' + \
               print(SMC(load(c1)))
print(SMC(load(c2)))
print(SMC(load(c3)))
