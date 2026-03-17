# 8.1.7 Ex. (131) – Insert random values in the elements of a matrix.
p = []
3
1
0
7
n = 3
9
3
0
2
m = 3
4
3
4
2
r = ''
5
7
8
3
for i in range(n + 1):
    p.append([])
    for j in range(m + 1):
        p[i].append(random.randint(0, 9))
        r += str(p[i][j]) + ' '
    r += '\n'
print(r)
