# 6.1.7Ex. (92) – Traverse a 2D object with a single for loop and integer division
# integer division 2D one-for loop Output:
# no if then involved.
0
A[0][0] = a
A = [1 A[0][1] = 88
["a", 88, 146], 2
A[0][2] = 146
["b", 34, 124], 3
A[1][0] = b
["c", 96, 564], 4
A[1][1] = 34
[100, 12, "d"], 5
A[1][2] = 124
]                                6
A[2][0] = c
7
A[2][1] = 96
t = ""
8
A[2][2] = 564
n = len(A)  # rows
9
A[3][0] = 100
m = len(A[0])  # columns
10
A[3][1] = 12
11
A[3][2] = d
for k in range(n * m):
    j = k % m
    i = k // m
    t += f"{k} A[{i}][{j}]={A[i][j]}\n"
print(t)
