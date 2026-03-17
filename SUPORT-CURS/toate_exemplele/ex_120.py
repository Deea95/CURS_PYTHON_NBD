# 7.1.26 Ex. (120) – Matrix multiplication with two for loops
a = [Output:
[2, 4, 6],
[3, 5, 6], 34
58
60
[3, 5, 4]
39
67
72
]                       33
57
64
b = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
]
i = j = 0
r = ""
c = []
n1 = len(a)
n2 = len(a[0])
q = n1 * n2
c.append([])
for v in range(q):
    j = v % n2
    if j == 0 and v != 0 and i < n1 and v != q:
        i += 1
    c.append([])
    r += "\n"
    c[i].append(0)
    for k in range(len(a[i])):
        c[i][j] += a[k][j] * b[i][k]
        r += str(c[i][j]) + " "
print(r)
