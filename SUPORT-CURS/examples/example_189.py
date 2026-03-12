a = {}
b = [3, 6, 2, 78, 99, 1, 4]
r = 0
n = len(b)
for i in range(n):
    a[b[i]] = b[i]
m = max(a.keys()) + 1
for j in range(m):
    if j in a:
        b[r] = a[j]
        r += 1
print(b)
Inside
the
loop, it
assigns
the
value
of
b[i]
t
the
number
of
elements), and stores
it in the
that
value
to
b[r] and increments
the
value
ranges and is written
for this book.To my
