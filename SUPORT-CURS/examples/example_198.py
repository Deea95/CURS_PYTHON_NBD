a = [0] * 9
n = 9
for k in range(n):
    a[k] = random.randint(0, 99)


def chart(a):
    m = 9
    t = [['' for _ in range(n)] for _
         # Use default=1 to avoid
         max_val = max(a, default=1)
    for j in range(m):
        for
    i in range(n):
    f = int((m / max_val) * a
    t[m - j - 1][i] = '\u2591
    if j < f:
        t[m - j - 1][i] = '\u


def SMC(a):
    n = len(a)
    m = len(a[0])
    r = ''
    for i in range(n + 2):
        for j in range(m):
            if i < n:
                r += a[i][j]
            if i == n:
                r += '|'
            if i > n:
                r += str(j + 1)
        if i == n:
            r += '\n'
        if i < n:
            r += "_" + str(n - i) + "


print(SMC(chart(a)))
print('\n' + str(a))
code
prints
the
result
of
the
SMC(chart(a))
fu
array
a and then
prints
a
visual
representation
block
characters(▓ ░) to
represent
the
d
is returned
at
the
end.The
SMC(a)
function
row,
with underscores(“_”) at the bottom, “
labels
for each column at the top.The resul
then
returned.In
the
end, the
code
prints
the
