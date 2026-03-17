# 10.4.7 Ex. (188) – Alphabet detection on matrices
c = [Output:
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 1, 1, 0, 1, 1], 1, 0
[1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
[1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
]

def matrix_alphabet(t):
    a = []
    n = len(t)
    m = len(t[0])
    for i in range(n):
        for j in range(m):
            q = 1
            for k in range(len(a) + 1):
                if k < len(a) and t[i][j] == a[k]:
                    q = 0
            if q == 1:
                a.append(t[i][j])
    return a


print(matrix_alphabet(c))
