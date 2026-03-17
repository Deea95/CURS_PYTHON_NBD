# 7.1.13 Ex. (107) – Show bottom – left part of the matrix
a = [Output:
[1, 2, 3, 4],
[5, 6, 7, 8], 1
[9, 0, 1, 2], 5
6
[3, 4, 5, 6]
9
0
1
]                             3
4
5
6
d = []
n = len(a)
r = ''
for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[i][j])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)
