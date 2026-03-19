# 7.1.7 Ex. (101) – Find max and min on columns and rows of a matrix

m = [
    [2, 4, 4],
    [3, 5, 6],
    [3, 5, 4]
]
a = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(len(m)):
    for j in range(len(m[i])):
        if not a[2][j]:
            a[2][j] = 10000
        if not a[3][i]:
            a[3][i] = 10000
        if a[0][j] < m[i][j]:
            a[0][j] = m[i][j]
        if a[1][i] < m[i][j]:
            a[1][i] = m[i][j]
        if a[2][j] > m[i][j]:
            a[2][j] = m[i][j]
        if a[3][i] > m[i][j]:
            a[3][i] = m[i][j]
print('C Max =', a[0])
print('R Max =', a[1])
print('C Min =', a[2])
print('R Min =', a[3])
# or an optimised version:
m = [
    [2, 4, 4],
    [3, 5, 6],
    [3, 5, 4]
]
a = [
    [0, 0, 0],
    [0, 0, 0],
    [10000, 10000, 10000],
    [10000, 10000, 10000]
]
for i in range(len(m)):
    for j in range(len(m[i])):
        a[0][j] = max(a[0][j], m[i][j])
        a[1][i] = max(a[1][i], m[i][j])
        a[2][j] = min(a[2][j], m[i][j])
        a[3][i] = min(a[3][i], m[i][j])
print('C Max =', a[0])
print('R Max =', a[1])
print('C Min =', a[2])
print('R Min =', a[3])
