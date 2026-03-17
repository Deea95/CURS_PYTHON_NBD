# 10.7.2 Ex. (195) – Average, standard deviation and coeficient of variation
def stat(a):              Output:


n = len(a)
b = 0
5.375,
e = 0
2.9246489410818914,
r = [0, 0, 0]  # AV, SD, CV 0.5441207332245379
for j in range(n):
    b += a[j]
r[0] = b / n
for j in range(n):
    e += (a[j] - r[0]) ** 2
r[1] = (e / (n - 1)) ** 0.5
r[2] = r[1] / r[0]
return r
a = [5, 1, 8, 4, 6, 2, 8, 9]
b = stat(a)
print(b)
