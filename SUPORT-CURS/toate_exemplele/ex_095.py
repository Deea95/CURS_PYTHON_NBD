# 7.1.1 Ex. (95) – How many 1's in matrix
# how many 1's in matrix.
a = [[1, 1, 0, 0, 0],
[0, 1, 0, 0, 1],
     [1, 0, 0, 1, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1]]
n = len(a)
m = len(a[0])
k = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            k += 1
print(k)
