# (third array).
a = [
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2]
]
b = [
    [1, 1, 0, 0, 0],
    [3, 1, 0, 0, 1],
    [1, 3, 0, 1, 1],
    [0, 0, 0, 7, 0],
    [3, 0, 4, 0, 9]
]
c = [
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 1]
]
n = len(a)
m = len(a[0])
r = ''
for i in range(n):
    r += '\n'
    for j in range(m):
        if b[i][j] == 0:
            c[i][j] = a[i][j] * c[i][j
            if b[i][j] == 1:
                c[i][j] = a[i][j] + c[i][j
            if b[i][j] == 2:
                c[i][j] = a[i][j] - c[i][j
            if b[i][j] == 3:
                c[i][j] = c[i][j] - a[i][j
            if b[i][j] == 4:
                c[i][j] = a[i][j] % c[i][j
            if b[i][j] == 5:
                c[i][j] = a[i][j] / c[i][j
            if b[i][j] == 6:
                c[i][j] = a[i][j]
            if b[i][j] == 7:
                c[i][j] = '#'
            if b[i][j] == 8:
                pass  # Placeholder for "d
            if b[i][j] == 9:
                if
            c[i][j] <= a[i][j]:
            c[i][j] = a[i][j]
            r += str(c[i][j]) + " "
            print(r)
            rows(indexed
            by
            i) and the
            other
            for colum
            checks the value of b[i][j] to determine whic
            the elements of a and c.(2) Ifb[i][j] is 1, i
            is 2, it subtracts the elements of c from a.(
            a from c.(5)I fb[i][j] is 4, it takes the modu
            of c to the corresponding element of a.(8)
            character “  # ”. (9) If b[i][ j] is 8, then the co
