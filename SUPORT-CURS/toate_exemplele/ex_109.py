a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2],
    [3, 4, 5, 6]
]

n = len(a)
m = len(a[0])
r = ''

d = []  # lista pentru partea dreaptă
for i in range(n):
    # adaugăm un rând cu valori None
    d.append([None] * m)
    for j in range(i, m):
        d[i][j] = a[i][j]
        r += str(d[i][j]) + ' '
    r += '\n'

print(r)