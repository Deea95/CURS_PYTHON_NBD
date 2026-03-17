# 5.1.42Ex. (82) – Average, standard deviation and coefficient of variation
a = [5, 6, 2, 9, 44, 200]
Output:
n = len(a)
AV = 44.333333333333336
b = 0
SD = 77.8322983514342
e = 0
CV = 1.7556157522879894
for j in range(n):
    b += a[j]
x = b / n
for j in range(n):
    e += (a[j] - x) ** 2
s = (e / (n - 1)) ** 0.5
c = s / x
print('AV =', x)
print('SD =', s)
print('CV =', c)
This
source
code is fundamental
for any scientist or/ and engineer, and it calculates and
