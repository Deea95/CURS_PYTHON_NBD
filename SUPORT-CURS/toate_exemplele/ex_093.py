# 6.1.8Ex. (93) – Traverse a 2D object with a single for loop using arithmetic operators
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
for k in range(n * m):
    9
    A[3][0] = 100
j = k % m
10
A[3][1] = 12
i = k(- j) // m
11
A[3][2] = d
t += str(k) + " A[" + str(i) + "][" + str(j) + "]="
t += str(A[i][j]) + "\n"
print(t)
