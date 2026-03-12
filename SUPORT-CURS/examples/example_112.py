a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2],
    [3, 4, 5, 6]
]
d = []
n = len(a)
r = ''
for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[j][i - j])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)
stored in the
d
array
at
the
same
position(d
