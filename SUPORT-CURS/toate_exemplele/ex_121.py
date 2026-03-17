# 7.1.27 Ex. (121) – Multiply specific elements of two matrices based on a map
a = [
[2, 4, 6],
[3, 5, 6],

[3, 5, 4]

]

b = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]
c = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
]
n = len(a)
m = len(a[0])
r = ''
for i in range(n):
    r += '\n'
    for j in range(m):
        if b[i][j] == 1:
            c[i][j] = a[i][j] * c[i][j]
        r += str(c[i][j]) + " "
print(r)
