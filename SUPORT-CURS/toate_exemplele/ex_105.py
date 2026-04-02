# 7.1.11 Ex. (105) – Sum all values from the left and right diagonal of a square matrix
a = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2],
[3, 4, 5, 6]
]
ld = 0
rd = 0
n = len(a)
m = len(a[0])
i = 0
for j in range(m):
    ld += a[i][j]
    rd += a[i][m - j - 1]
    i += 1
print('L=' + str(ld) + '|R=' + str(rd))

"""se da matrice
a = [1, 2, 3],
    [4,5,6],
    [7,8,9]
    calculati produsul diagonalelor"""
a = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9]
]

ld = 1  # produsul diagonalei principale
rd = 1  # produsul diagonalei secundare
n = len(a)
m = len(a[0])

i = 0
for j in range(m):
    ld *= a[i][j]          # înmulțim elementele diagonalei principale
    rd *= a[i][m - j - 1]  # înmulțim elementele diagonalei secundare
    i += 1

print('Produs diagonala stanga=' + str(ld) + '| diagonala dreapta=' + str(rd))
