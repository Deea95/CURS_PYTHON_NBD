# 7.1.22 Ex. (116) – Matrix flip horizontal
# flip horisontal.               Output:
a = [4 3 2 1
[1, 2, 3, 4], 8 7 6 5
     [5, 6, 7, 8], 2 1 0 9
     [9, 0, 1, 2], 6 5 4 3
     [3, 4, 5, 6]
     ]
d = []
n = len(a)
m = len(a[0])
r = ''
for i in range(n):
    d.append([])
    for j in range(m):
        d[i].append(a[i][m - j - 1])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)
