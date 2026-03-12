a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = [1, 1, 1, 4, 4, 4, 6]
l = len(a) - 1
for k in range(0, l + 1):
    c[k] = a[c[k]] + b[k]
print("c =", c)
the
values[2, 3, 4, 5, 9, 8, 3], array
b
contai
set
to[1, 1, 1, 4, 4, 4, 6].The
variable
l is
(i.e., l−1).Inside
the
loop, each
element
of
is assigned
the
value
of
a[c[k]] + b[k].Thi
5
Dynamically
Resizable
Arrays(Lists)
print(“c = ” + c);.Thus, this
code
modifies
