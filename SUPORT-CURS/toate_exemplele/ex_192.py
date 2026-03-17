# 10.6.1 Ex. (192) – Get all permutations of a given string (I)
a = []
Output:


def permute(s, r, l):             ACTG,


if l == r:                      ACGT,
a.append(s)
ATCG,
else:                           ATGC,
for i in range(l, r + 1):     AGTC,
s = swap(s, l, i)
AGCT,
s = swap(s, l, i)


def swap(s, i, j):
    c = list(s)
    t = c[i]
    c[i] = c[j]
    c[j] = t
    return ''.join(c)


s = "ACTG"
n = len(s)
TGAC,
print(a)
GCTA,
