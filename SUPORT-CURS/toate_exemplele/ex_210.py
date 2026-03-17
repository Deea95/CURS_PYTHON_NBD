# 11.1.4 Ex. (210) – Decompose a matrix into multiple matrices based on unique values
def matrix_alphabet(t):           Output:


a = []
n = len(t)
M1
m = len(t[0]) - ---------
for i in range(n):              |
    1
1
1
1
11 |
for j in range(m):
    q = 1
    for k in range(len(a) + 1):
        if k < len(a) and t[i][j] == a[k]:
            q = 0
    if q == 1:
        a.append(t[i][j])
return a


def decompose(c, a):              M2


n = len(c) - ---------
m = len(c[0]) | 0 |
d = [] | 0
0 |
for i in range(n):             |
    0
0
00 |
d.append([]) | 0
0
0 |
for j in range(m):
    d[i].append([])
    for k in range(len(a) + 1):
        d[i][j].append(" ")  # "\u2591"
        if k < len(a) and c[i][j] == a[k]:
            d[i][j][k] = c[i][j]
return d
return d


def SMC(m, k):
    r = 'M' + str(k + 1) | 2 |
    r += '\n ----------\n' | 2 |
    for i in range(len(m)):         |
    2 |
    r += "|" | 2 |
    for j in range(len(m[i])):    | |
    r += str(m[i][j][k]) | |


r += "|\n" | |
r += ' ----------' | |
return r - ---------
# Main code                        ----------
r = "u" | |
c = [ | 3 |
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1], | 3 |
                                      [1, 2, 1, 0, 1, 3, 1, 0, 1, 1], | 3 |
                                                                        [1, 1, 2, 0, 1, 3, 0, 1, 0, 1],
[0, 1, 0, 2, 1, 3, 1, 0, 0, 1],
[1, 1, 1, 0, 2, 3, 1, 0, 1, 0],
[1, 0, 1, 1, 1, 3, 0, r, 0, 0],
[1, 0, 3, 3, 3, 3, r, 0, 0, 1],
[1, 0, 1, 1, 1, r, 0, 9, 9, 9],
[1, 1, 0, 0, 0, 0, 1, 9, 0, 9]
]
b = matrix_alphabet(c)
t = decompose(c, b) | |
for k in range(len(b)):            | |
print(SMC(t, k)) | |
print(b) | u |
