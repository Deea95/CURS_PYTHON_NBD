# 7.1.16 Ex. (110) – Show top – right part of the matrix and flip 90 degrees left
a = [Output:
[1, 2, 3, 4],
[5, 6, 7, 8], 1
[9, 0, 1, 2], 6
2
[3, 4, 5, 6]
1
7
3
]                             6
2
8
4
d = []
n = len(a)
r = ''
for i in range(n):              1
2
3
4
d.append([]) - 6
7
8
for j in range(i + 1):       - - 1
2
d[i].append(a[i - j][i]) - - - 6
r += str(d[i][j]) + ' '
r += '\n'                    '''                     
          print(r)
