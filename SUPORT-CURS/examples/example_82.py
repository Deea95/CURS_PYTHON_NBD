a = [5, 6, 2, 9, 44, 200]
n = len(a)
b = 0
e = 0
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
for any s
    prints
    three
    statistical
    measures(average, sta
    for a given array of numbers.The code begi
    sum of squared differences (e) from the me
    the formula for sample standard deviation.It
    s by the mean x.The results are then print
    displaying the average (AV), standard devia
    for a given array of numbers, providing insig
