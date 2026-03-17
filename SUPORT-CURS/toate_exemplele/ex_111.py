# 7.1.17 Ex. (111) – Show top – right, flip 90 degrees left and flip horizontally
a = [Output:
[1, 2, 3, 4],
[5, 6, 7, 8], 1
[9, 0, 1, 2], 2
6
[3, 4, 5, 6]
3
7
1
]                             4
8
2
6
d = []
n = len(a)
r = ''
for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[j][i])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)
