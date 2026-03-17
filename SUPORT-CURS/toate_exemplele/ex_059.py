# 5.1.19Ex. (59) – Add forward and reverse values and subtract max
a = []
Output:
b = []
c = []
a = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
b = 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
# In Python, range(11)
c = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
# generates numbers from
# 0 to 10 inclusive.
for j in range(11):
    a.append(j)
    b.append(10 - j)
    c.append(a[j] + b[j] - 10)
print("a =", a)
print("b =", b)
print("c =", c)
