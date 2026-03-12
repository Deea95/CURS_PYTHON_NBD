a = [[1, 1, 0, 0, 0],
     [0, 1, 0, 0, 1],
     [1, 0, 0, 1, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1]]
n = len(a)
m = len(a[0])
k = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            k += 1
print(k)
the
matrix
a( in this
case, there
are
5
rows).
in the
matrix
a( in this
case, there
are
5
colu
as a[i][j], is equal
to “1”.If
it is, the
k
var
then
prints
the
value
of
k
to
the
output, wh
