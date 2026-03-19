a = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
]
b = [
    [0, 0, 1],
    [1, 1, 0],
    [0, 0, 1]
]
n = len(a)
m = len(a[0])
r = 0
for i in range(n):
    for j in range(m):
        if b[i][j] == 1:
            r += a[i][j]
print(r)
