# 10.1.5 Ex. (169) – A function to correctly display a matrix
def ps(a, s):                     Output:


t = ""
b = s - (len(str(a)) % s)
20
4
60
for i in range(b):              39
5
60
t += " "
3
50
40
return t


def SMC(m):
    r = "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += str(m[i][j]) + ps(m[i][j], 3)
        r += "\n"
    return r


m = [
    [20, 4, 60],
    [39, 5, 60],
    [3, 50, 40]
]
print(SMC(m))
