# 11.1.5 Ex. (211) – Count islands over the matrix and show their location
a = [Output:
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 1, 0, 0, 1, 1], Islands = 3
[1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 2
0
2
2
2
2
0
3
3
3
[1, 1, 1, 0, 1, 1, 1, 0, 1, 0], 2
0
2
0
2
2
0
0
3
3
[1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
2
0
2
2
2
2
0
0
0
0
]                           2
0
0
0
0
0
0
0
0
4
b = [2 2 0 0 0 0 0 0 0 4
[+1, 0],  # right side element.
     [-1, 0],  # left side element.
     [0, +1],  # upward side element.
     [0, -1],  # downward side element.
     [+1, +1],  # upward-right side element.
     [-1, -1],  # downward-left side element.
     [+1, -1],  # downward-right side element.
     [-1, +1]  # upward-left side element.
     ]


def d(a, i, j, n, m, c):
    if i < 0 or j < 0 or i > (n - 1) or \
            j > (m - 1) or a[i][j] != 1:
        return
    if a[i][j] == 1:
        a[i][j] = c + 1
        for k in range(len(b)):
            d(a, i + b[k][0], j + b[k][1], n, m, c)


def SCAN(a):
    n = len(a)  # row.
    m = len(a[0])  # col.
    c = 0  # islands.
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                c += 1
    return c


def SMC(m):
    r = "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += str(m[i][j]) + " "
        r += "\n"
    return r


print("Islands =", SCAN(a))
print(SMC(a))
