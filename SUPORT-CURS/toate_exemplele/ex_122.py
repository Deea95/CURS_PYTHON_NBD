# 7.1.28 Ex. (122) – Different operations based on maps
# perform different operations between Output:
# the values of the homologous elements
# of two arrays based on a map/model 5 5 6 6 6
# (third array).                   1 5 6 6 5
a = [
[2, 2, 2, 2, 2],
     [2, 2, 2, 2, 2],
     [2, 2, 2, 2, 2],
     [2, 2, 2, 2, 2],
     [2, 2, 2, 2, 2]
     ]
b = [
    [1, 1, 0, 0, 0],
    [3, 1, 0, 0, 1],
    [1, 3, 0, 1, 1],
    [0, 0, 0, 7, 0],
    [3, 0, 4, 0, 9]
]
c = [
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 1]
]
n = len(a)
m = len(a[0])
r = ''
for i in range(n):
    r += '\n'
    for j in range(m):
        if b[i][j] == 0:
            c[i][j] = a[i][j] * c[i][j]
        if b[i][j] == 1:
            c[i][j] = a[i][j] + c[i][j]
        if b[i][j] == 2:
            c[i][j] = a[i][j] - c[i][j]
        if b[i][j] == 3:
            c[i][j] = c[i][j] - a[i][j]
        if b[i][j] == 4:
            c[i][j] = a[i][j] % c[i][j]
        if b[i][j] == 5:
            c[i][j] = a[i][j] / c[i][j]
        if b[i][j] == 6:
            c[i][j] = a[i][j]
        if b[i][j] == 7:
            c[i][j] = '#'
        if b[i][j] == 8:
            pass  # Placeholder for "do stuff"
        if b[i][j] == 9:
            if c[i][j] <= a[i][j]:
                c[i][j] = a[i][j]
        r += str(c[i][j]) + " "
print(r)
