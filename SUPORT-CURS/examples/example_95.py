# how many 1's in matrix.
a = [[1, 1, 0, 0, 0],
n = len(a)
m = len(a[0])
k = 0
for i in range(n):
    for j in range(m):
        if a[i][j ] ==1 :
            print(k)