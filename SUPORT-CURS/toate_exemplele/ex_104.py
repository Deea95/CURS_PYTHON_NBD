# 7.1.10 Ex. (104) – Sum all values from the left diagonal of the square matrix
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
    d += a[i][j]
    print(a[i][j])
    i += 1
print('---\n' + str(d))
