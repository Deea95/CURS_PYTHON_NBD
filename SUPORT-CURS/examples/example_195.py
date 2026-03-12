def stat(a):
    n = len(a)
    b = 0
    e = 0
    r = [0, 0, 0]  # AV, SD, CV
    for j in range(n):
        b += a[j]
    r[0] = b / n
    for j in range(n):
        e += (a[j] - r[0]) ** 2
    r[1] = (e / (n - 1)) ** 0.5
    r[2] = r[1] / r[0]


a = [5, 1, 8, 4, 6, 2, 8, 9]
b = stat(a)
print(b)
the
average(AV;
mathematically
denoted as
denoted as σ), and the
coefficient
of
variation
x = i = 1
i = i
n(x − x)2
n−1(a[i] −
σ = i = 1
i = i = 0
Cv = =
(AV) is calculated
by
dividing
the
sum
b
by
t
and the
result is stored in r[0].The
code
th
differences
from the average

(e)
for each ele
calculating the standard deviation (SD).The
result is stored in r[1].The coefficient of va
standard deviation to the average (r[1] / r[0]).
import for the math library and the sqrt fun
square root of the variance.The expression (
notice further that q0.5 × q0.5 = q0.5+0.5 = q
