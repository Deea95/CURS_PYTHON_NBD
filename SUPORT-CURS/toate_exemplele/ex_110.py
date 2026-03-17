a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 0, 1, 2], 
    [3, 4, 5, 6]
]

n = len(a)
r = ''
d = []

for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[i - j][i])
        r += str(d[i][j]) + ' '
    r += '\n'

print(r)