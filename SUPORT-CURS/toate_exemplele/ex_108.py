# 7.1.14 Ex. (108) – Show bottom – left part of the matrix and flip horizontal
a = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2],
[3, 4, 5, 6]

]

d = []
n = len(a)
m = len(a[0])
r = ''
for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[i][i - j])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)
