# 10.7.4 Ex. (197) – Vertical chart from the array with pre-declared values
def smc(m):                           Output:


r = ''
for row in m:                      ░░░░░▓░░
for val in row:                  ░░░░░▓░░
r += val                       ░░░░░▓░░
r += "\n"                        ░░░░░▓░▓
return r                           ░░▓░░▓▓▓
a = [5, 2, 8, 4, 6, 12, 8, 9]         ▓░▓░▓▓▓▓
m = 10
n = len(a)
max_value = max(a)
t = [['' for _ in range(n)] for _ in range(m)]
for j in range(m):
    for i in range(n):
        f = (m * a[i]) // max_value
        # Light shade character.
        t[m - j - 1][i] = '\u2591'
        if j < f:
            # Dark shade character.
            t[m - j - 1][i] = '\u2593'
print(smc(t))
The
application
from above shows

how
an
ASCII(American
Standard
Code
for Infor -
