# 7.1.6 Ex. (100) – Sum all values from the colums of the matrix
m = [
[2, 4, 4],
[3, 5, 6],
[3, 5, 4]
]
c = []
for i in range(len(m)):
    for j in range(len(m[i])):
        if len(c) <= j:
            c.append(0)
        c[j] += m[i][j]
        # c[j] *= m[i][j]
print(c)
