# 7.1.18 Ex. (112) – Secondary diagonal scan (right)
a = [Output:
[1, 2, 3, 4],
[5, 6, 7, 8], 1
[9, 0, 1, 2], 2
5
[3, 4, 5, 6]
3
6
9
]                             4
7
0
3
d = []
n = len(a)
r = ''
for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[j][i - j])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)
