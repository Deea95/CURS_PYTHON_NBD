a = [
    [1.0, 0.0, 0.0, 0.0],
    [0.5, 0.0, 0.5, 0.0],
    [0.0, 0.5, 0.0, 0.5],
    [0.0, 0.0, 1.0, 0.0]
]

v = [
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

C = 5
n = len(a)
m = len(a[0])

for k in range(1, C + 1):

    for i in range(n):
        for j in range(m):
            v[1][j] += v[0][i] * a[i][j]

    for i in range(m):
        v[0][i] = v[1][i]
        v[1][i] = 0

    print(f'k({k}) = {v[0]}')