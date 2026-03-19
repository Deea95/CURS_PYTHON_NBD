a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2],
    [3, 4, 5, 6]
]
ld = 0
rd = 0
n = len(a)
m = len(a[0])
i = 0
for j in range(m):
    ld += a[i][j]
    rd += a[i][m - j - 1]
    i += 1
print('L=' + str(ld) + '|R=' + str(rd))
diagonal), both
initially
set
to
0.
These
varia
(which is 4 in this
case), and m
represents
th
loop, two
actions
are
performed.The
ld(left
value
of
the
current
element
a[i][j].This
st
left
diagonal
of
the
matrix.The
rd(right
dia
element
at
a[i][m - j - 1].This
step
accumulate
are
presented in the
following
format: “L = ld
