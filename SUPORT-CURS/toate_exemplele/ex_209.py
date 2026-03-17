# 11.1.3 Ex. (209) – The general logic gate based on a map
def g(a, b, t):

    h = [
    [0, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 0, 0, 1]
    ]
    for i in range(len(h)):
        if a == h[i][0] and b == h[i][1]:
            return h[i][t + 1]
a = [
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 0]
]

b = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

c = []
n = len(a)
m = len(a[0])
r = ''

for i in range(n):
    r += '\n'
    c.append([])
    for j in range(m):
        c[i].append(g(a[i][j], b[i][j], 6))
        r += str(c[i][j]) + " "
print(r)
