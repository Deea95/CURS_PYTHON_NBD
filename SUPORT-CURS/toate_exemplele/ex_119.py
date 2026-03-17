# 7.1.25 Ex. (119) – Matrix multiplication with three for loops
a = [
[2, 4, 6],
[3, 5, 6],
[3, 5, 4]

]

b = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
]
c = []
r = ""
for i in range(len(a)):
    r += "\n"
    c.append([])
    for j in range(len(a[i])):
        c[i].append(0)
        for k in range(len(a[i])):
            c[i][j] += a[k][j] * b[i][k]
        r += str(c[i][j]) + " "
print(r)
