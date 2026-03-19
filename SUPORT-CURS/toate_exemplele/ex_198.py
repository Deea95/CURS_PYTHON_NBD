import random

n = 9
a = [0] * n

# generare valori random
for k in range(n):
    a[k] = random.randint(0, 99)


def chart(a):
    m = 9
    t = [['' for _ in range(n)] for _ in range(m)]

    # evită împărțirea la 0
    max_val = max(a, default=1)

    for j in range(m):
        for i in range(n):
            f = int((m / max_val) * a[i])
            t[m - j - 1][i] = '\u2591'
            if j < f:
                t[m - j - 1][i] = '\u2593'

    return t


def SMC(a):
    n = len(a)
    m = len(a[0])
    r = ''

    for i in range(n + 2):
        for j in range(m):
            if i < n:
                r += a[i][j]
            elif i == n:
                r += '|'
            else:
                r += str(j + 1)

        if i == n:
            r += '\n'
        elif i < n:
            r += "_" + str(n - i) + "\n"

    return r


print(SMC(chart(a)))
print('\n' + str(a))