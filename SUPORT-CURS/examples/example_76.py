# a = 'abcdef'
# b = list(a)
b = ['a', 'b', 'c', 'd', 'e', 'f']
n = len(b)
c = [None] * n
for i in range(n):
    c[i] = b[n - i - 1]
print(c)
that
iterates
from i = 0
toi = n−1(inclus
b[n−i−1] to
the
corresponding
index in arra
