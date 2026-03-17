# 6.1.2Ex. (87) – Accessing the elements of matrix A using nested for loops
A = [Output:
["a", 88, 146],
["b", 34, 124], A[0][0] = a
["c", 96, 564], A[0][1] = 88
[100, 12, "d"],
A[0][2] = 146
]
A[1][0] = b
A[1][1] = 34
t = ""
A[1][2] = 124
A[2][0] = c
for i in range(len(A)):
    A[2][1] = 96
for j in range(len(A[i])):
    A[2][2] = 564
t += "\n A[{}][{}]={}".format(i, j, A[i][j])
A[3][0] = 100
print(t)
A[3][1] = 12
A[3][2] = d
