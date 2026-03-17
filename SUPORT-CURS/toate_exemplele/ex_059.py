# 5.1.19Ex. (59) – Add forward and reverse values and subtract max
a = []
b = []
c = []

# In Python, range(11)
# generates numbers from
# 0 to 10 inclusive.
for j in range(11):
    a.append(j)
    b.append(10 - j)
    c.append(a[j] + b[j] - 10)
print("a =", a)
print("b =", b)
print("c =", c)
