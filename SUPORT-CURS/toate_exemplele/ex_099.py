# 7.1.5 Ex. (99) – Sum all values from the rows of the matrix
m = [Output:
[2, 4, 4],
[3, 5, 6], 10, 14, 12
[3, 5, 4]
]
r = []
for i in range(len(m)):
    # Initialize r[i] to 0.
    r.append(0)
    for j in range(len(m[i])):
        r[i] += m[i][j]
print(r)
