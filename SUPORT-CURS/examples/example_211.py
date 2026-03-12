a = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
]
b = [
    [+1, 0],  # right side element.
    [-1, 0],  # left side element.
    [0, +1],  # upward side element.
    [0, -1],  # downward side elemen
    [+1, +1],  # upward-right side el
    [-1, -1],  # downward-left side e
    [+1, -1],  # downward-right side
    [-1, +1]  # upward-left side ele
]


def d(a, i, j, n, m, c):
    if i < 0 or j < 0 or i > (n - 1) or \
            j > (m - 1) or a[i][j] != 1:
        if a[i][j] == 1:
            a[i][j] = c + 1
            for k in range(len(b)):
                d(a, i + b[k][0], j + b[k][1],


def SCAN(a):
    n = len(a)  # row.
    m = len(a[0])  # col.
    c = 0  # islands.
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                c += 1
                d(a, i, j, n, m, c)


def SMC(m):
    r = "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += str(m[i][j]) + " "
        r += "\n"


print("Islands =", SCAN(a))
print(SMC(a))
downward, etc.) for navigating neighboring e
(i, j).It explores neighboring elements and
each new landmass found.Function SCAN(
(regions of connected land elements).It
init
(r)
where
each
row
of
the
matrix is separated
found
by
calling
SCAN(a) and prints
the
ent
the
SMC(a)
function.
