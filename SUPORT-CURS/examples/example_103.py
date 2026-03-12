a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
d = 0
n = len(a)
m = len(a[0])
i = 0
j = 0
d += a[i][m - j - 1]
print(a[i][m - j - 1])
i += 1
j += 1
print('---\n' + str(d))
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
d = 0
n = len(a)
m = len(a[0])
i = 0
for j in range(m):
    d += a[i][m - j - 1]
    print(a[i][m - j - 1])
    i += 1
print('---\n' + str(d))
the
code
shows
a
print
statement
within
the
print
statement
that
displays
a
line
containin
i += 1 is meant
to
increment
the
i
counter in
code
can
be
reduced
to
a
single
loop(see
the
