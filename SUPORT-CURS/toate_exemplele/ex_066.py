# 5.1.26Ex. (66) – Which is bigger between n and n + 1 ? (optimisation)
a = [2, 3, 4, 5, 9, 8, 3, 8, 3]
Output:
l = len(a) - 1
t = ' '
r = '<'
for k in range(0, l):
    if a[k] > a[k + 1]:
        r = ">"
    t += r
    r = "<"
print(t)
This
code
begins
by
defining
an
array
a
containing
a
sequence
of
integers, namely[2,
3, 4, 5, 9, 8, 3, 8, 3].The
variable
l is then
initialized
to
store
the
length
of
the
array
minus
