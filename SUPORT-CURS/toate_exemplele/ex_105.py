# 7.1.11 Ex. (105) – Sum all values from the left and right diagonal of a square matrix
a = [Output:
[1, 2, 3, 4],
[5, 6, 7, 8], L = 14 | R = 14
[9, 0, 1, 2],
[3, 4, 5, 6]
]
ld = 0
rd = 0
n = len(a)
m = len(a[0])
i = 0
for j in range(m):
    ld += a[i][j]
    rd += a[i][m - j - 1]
    i += 1
print('L=' + str(ld) + '|R=' + str(rd))
