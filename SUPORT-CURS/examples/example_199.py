# 10.7.6 Ex. (199) – Shannon entropy
import math


def entropy(c):
    a = alpha(c)
    n = len(a)
    k = len(c)
    e = 0
    for i in range(n):
        r = len(c.replace(a[i], ''))
        a[i] = (k - r) / k
        # e += -a[i] * log(2, a[i])
        e += a[i] * log(2, 1 / a[i])
    return e


# ALPHABET DETECTION.
def alpha(c):
    a = []
    t = list(c)
    k = len(t)
    for i in range(k):
        q = 1
        for j in range(len(a)):
            if t[i] == a[j]:
                q = 0
        if q == 1:
            a.append(t[i])
    return a


def log(n, v):
    return math.log(v) / math.log(n)


print(entropy('uiuhd87wqsaidhsad'))
