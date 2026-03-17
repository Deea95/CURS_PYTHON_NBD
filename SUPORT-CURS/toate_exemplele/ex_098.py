# 7.1.4 Ex. (98) – Multiplication involving a scalar and a matrix.
m = [Output:
[2, 4, 6],
[3, 5, 6], 6, 12, 18, 9, 15, 18, 9, 15, 12
[3, 5, 4]
]
s = 3  # scalar
for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j] = s * m[i][j]
        # m[i][j] *= s
print(m)
