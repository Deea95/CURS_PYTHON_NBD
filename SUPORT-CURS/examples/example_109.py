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
    d.append([None] * m)
    for j in range(i, m):
        d[i][j] = a[i][j]
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)
the
outer
loop, a
nested
loop(controlled
by
up
to
the
last
column
m(exclusive).During
stage, the
code
prints
the
contents
of
the
r
