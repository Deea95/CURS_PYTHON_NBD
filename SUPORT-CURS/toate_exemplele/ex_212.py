# 11.1.6 Ex. (212) – Count islands over the matrix and count the characters in each
a = [Output:
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 1, 0, 0, 1, 1], Islands = 3
[1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 1], *0 * * * * 0  # # #
[1, 1, 1, 0, 1, 1, 1, 0, 1, 0], *0 * 0 * * 0
0  # #
[1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
]
b = [
    [1, 0],  # right side.
    [-1, 0],  # left side.
    [0, 1],  # upward side.     34,8,5
    [0, -1],  # downward side.
    [1, 1],  # upward-right side.
    [-1, -1],  # downward-left side.
    [1, -1],  # downward-right side.
    [-1, 1]  # upward-left side.
]
q = ['*', '#', '%', '&']
p = []


def d(a, i, j, n, m, c):
    if i < 0 or j < 0 or i >= n or \
            j >= m or a[i][j] != 1:
        return
    if a[i][j] == 1:
        a[i][j] = q[c - 1]
        p[c - 1] += 1
        for k in b:
            d(a, i + k[0], j + k[1], n, m, c)


def SCAN(a):
    n = len(a)  # row.
    m = len(a[0])  # col.
    c = 0  # islands.
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                c += 1
                p.append(0)
    return c


def SMC(m):
    r = "\n"
    for row in m:
        for element in row:
            r += str(element) + " "
        r += "\n"
    return r


print("Islands =", SCAN(a))
print(SMC(a))
print(p)
