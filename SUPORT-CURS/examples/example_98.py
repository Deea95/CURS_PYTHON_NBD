m = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
]
s = 3  # scalar
for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j] = s * m[i][j]
        # m[i][j] *= s
print(m)
This
operator
multiplies
the
value
of
m[i][j
