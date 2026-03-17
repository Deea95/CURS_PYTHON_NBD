# 6.1.4Ex. (89) – Traverse a matrix with a single for loop (II)
A = [Output:
["a", 88, 146],
["b", 34, 124], 0
A[0][0] = a
["c", 96, 564], 1
A[0][1] = 88
[100, 12, "d"],
2
A[0][2] = 146
]
3
A[1][0] = b
4
A[1][1] = 34
t = ""
5
A[1][2] = 124
n = len(A)  # rows
6
A[2][0] = c
m = len(A[0])  # columns
7
A[2][1] = 96
8
A[2][2] = 564
i = 0
9
A[3][0] = 100
j = 0
10
A[3][1] = 12
for v in range(n * m):        11
A[3][2] = d
j = v % m
if v != 0 and j == 0:
    i += 1
t += f"{v} A[{i}][{j}]={A[i][j]}\n"
print(t)
