# 10.7.5 Ex. (198) – Vertical chart from array with random values at each run
a = [0] * 9                       ░░░░▓░░░░_9
n = 9                             ▓░░░▓░░░░_8
for k in range(n):                ▓░▓▓▓▓▓░░_6
a[k] = random.randint(0, 99)   ▓░▓▓▓▓▓▓░_5


def chart(a):                     ▓

    ░▓▓▓▓▓▓▓_3
m = 9
t = [['' for _ in range(n)] for _ in range(m)]
# Use default=1 to avoid
# division by zero.
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
            if i == n:
                r += '|'
            if i > n:
                r += str(j + 1)
        if i == n:
            r += '\n'
        if i < n:
            r += "_" + str(n - i) + "\n"
    return r


print(SMC(chart(a)))
print('\n' + str(a))
