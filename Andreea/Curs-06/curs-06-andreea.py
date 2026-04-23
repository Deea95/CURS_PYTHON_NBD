"""
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
print(entropy('aaaaabbbbb'))
print(entropy('ababababababababa'))
print(entropy('aabbbbbbbbbbbbbbb'))
"""
# 11.1.1 Ex. (207) – Spectral forecast for signals in Python.

# Spectral forecast for signals in Python.

A = '10.3,23.4,44.8,63.2,44.1,35.1,46.5,62.6,50.4'
B = '18.8,43.1,52.2,45.5,46.8,46.6,67.9,66.3,70.4'
M = ''

tA = A.split(',')
tB = B.split(',')

maxA = max(map(float, tA))
maxB = max(map(float, tB))
max_value = max(maxA, maxB)

d = 33

for i in range(len(tA)):
    v=((d/maxA)*float(tA[i]))+(((max_value-d)/maxB)*float(tB[i]))
    M += '{:.2f}'.format(v)
    if i < len(tA)-1:
        M += ','
print('Signal A:' + A)
print('Max(A[i]):' + str(maxA))
print('Signal M:' + M)
print('Signal B:' + B)
print('Max(B[i]):' + str(maxB))
