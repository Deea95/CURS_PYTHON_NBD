# 6.1.3Ex. (88) – Traverse a matrix with a single for loop (I)
m = [Output:
[2, 4, 6],
[3, 5, 6], m[0][0] = 2
[3, 5, 4]
m[0][1] = 4
]
m[0][2] = 6
m[1][0] = 3
i = j = 0
m[1][1] = 5
n1 = len(m)
m[1][2] = 6
n2 = len(m[0])
m[2][0] = 3
q = n1 * n2
m[2][1] = 5
m[2][2] = 4
for v in range(q):
    j = v % n2
    if j == 0 and v != 0 and i < n1 and v != q:
        i += 1
    print("m[{}][{}]={}".format(i, j, m[i][j]))
