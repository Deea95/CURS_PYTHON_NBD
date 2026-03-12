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
    [1, 0],  # right.
    [-1, 0],  # left.
    [0, 1],  # upward.
    [0, -1],  # downward.
    [1, 1],  # upward-right.
    [-1, -1],  # downward-left.
    [1, -1],  # downward-right.
    [-1, 1],  # upward-left.
]
q = ['*', '#', '%', '&', '@', '$', '!', '+'
     p = [[], [], []]


def d(a, i, j, n, m, c):
    if i < 0 or j < 0 or i > (n - 1) or \
            j > (m - 1) or a[i][j] != 1:
        a[i][j] = q[c - 1]
    p[1][c - 1] += 1
    for k in range(len(b)):
        d(a, i + b[k][0], j + b[k][1], n, m,


def scan(a):
    n = len(a)  # row.
    m = len(a[0])  # col.
    c = 0  # islands.
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                c += 1
                p[0].append(q[c - 1]
                p[1].append(0)
                d(a, i, j, n, m, c)
                for i in range(c):
                    p[2].append(f"{round((100 / (n * m)) * p[1


def smc(m, f):
    r = ''
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += str(m[i][j]) + \
                 ps(str(m[i][j]), f)
        r += '\n'


def ps(a, f):
    t = ''
    b = f - (len(a) % f)
    for i in range(b):
        t += ' '


print('Islands =', scan(a), '\n')
print(smc(a, 1))
print(smc(p, 4))
sent
movement in different
directions(right,
           calls
the
SCAN(a)
function, which
scans
the
prints
the
number
of
islands
found and two
above).Inside, the
SCAN(a)
function
scans
t
land
element(1).It
keeps
track
of
the
numbe
n, m, c) function is a
recursive
function
used
if the
current
position is within
bounds and
neighboring
positions.The
SMC(m, f)
func
in the
matrix
for alignment.The ps(a, f) fun
