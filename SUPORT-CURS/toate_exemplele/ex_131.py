# 8.1.7 Ex. (131) – Insert random values in the elements of a matrix.
import random

p = []

n = 3

m = 3

r = ''

for i in range(n + 1):
    p.append([])
    for j in range(m + 1):
        p[i].append(random.randint(0, 9))
        r += str(p[i][j]) + ' '
    r += '\n'
print(r)
