# 7.1.12 Ex. (106) – Sum all values from the left and right diagonal by using conditions
# Sum on principal and secondary diagonals. Output:
a = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2],
[3, 4, 5, 6]
]
d = [0, 0]
n = len(a)
m = len(a[0])
for i in range(n):
    for j in range(m):
        if i == j:
            d[0] += a[i][j]
        if i + j == n - 1:
            d[1] += a[i][j]
print('L=' + str(d[0]) + '|R=' + str(d[1]))
