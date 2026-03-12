a = [5, 2, 8, 4, 6, 22, 8, 9]
m = 15
c = '#'
t = ''
max_value = 0
n = len(a)
for i in range(n):
    if a[i] > max_value:
        max_value = a[i]
for i in range(n):
    f = int((m / max_value) * a[i])
    for k in range(f):
        t += c
    t += '\n'
print(t)
are
initialized: (1)
Variable
m is set
to
15.
character
used
to
visualize
the
data.(3)
Varia
characters
to
create
a
visual
representation.(
    (a[i]) is greater
than
the
current
maximum(m
with the value of a[i].This loop effectively
value) * a[i]).This computes a scaled value
value) and scales
it
to
fit
within
the
range
o
