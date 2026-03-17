# 7.1.9 Ex. (103) – Sum all values from the right diagonal of the square matrix
a = [Output:
[1, 2, 3],
[4, 5, 6], 3
[7, 8, 9]
5
]                       7
d = 0
n = len(a)
m = len(a[0])
i = 0
while i < n:
    j = 0
    while j < m:
        d += a[i][m - j - 1]
        print(a[i][m - j - 1])
        i += 1
        j += 1
print('---\n' + str(d))
# or a second version:
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
d = 0
n = len(a)
m = len(a[0])
i = 0
for j in range(m):
    d += a[i][m - j - 1]
    print(a[i][m - j - 1])
    i += 1
print('---\n' + str(d))
