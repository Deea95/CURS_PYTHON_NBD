import random

def mutate(a):
    n = len(a)
    m = len(a[0])
    q = 200

    for k in range(q):
        S = 0
        b = []

        for i in range(n):
            b.append([])

            for j in range(m):
                val = round(random.random())
                b[i].append(val)

                if val != a[i][j]:
                    S += 1

        if S >= m * n:
            return b

    return "not found by random means."


def smc(mat):
    if isinstance(mat, str):
        return mat

    r = ""
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            r += str(mat[i][j]) + " "
        r += "\n"
    return r


a = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]

print(smc(mutate(a)))