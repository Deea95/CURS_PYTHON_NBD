# 7.1.2 Ex. (96) – Sum all values from matrix elements
m = [Output:
[2, 4, 6],
[3, 5, 6], 38
[3, 5, 4]
]
r = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        r += m[i][j]
print(r)
