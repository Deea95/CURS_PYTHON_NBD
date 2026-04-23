import random

a = [1, 0, 0, 1, 1, 1, 0]
b = [0] * len(a)

n = 100
m = len(a)

C = [[None for _ in range(m + 1)] for _ in range(n)]

def mutate(c):
    p = 20  # %
    q = round(m * (1 - p / 100))
    k = 0

    for i in range(n):
        S = 0

        for j in range(m):
            b[j] = round(random.random())
            c[k][j] = b[j]

            if b[j] == a[j]:
                S += 1

        if S >= q:
            c[k][m] = S
            k += 1

    return c[:k]


def SMC(mat):
    r = ""
    for row in mat:
        r += ' '.join(str(x) for x in row) + "\n"
    return r


fit = mutate(C)
print(SMC(fit))