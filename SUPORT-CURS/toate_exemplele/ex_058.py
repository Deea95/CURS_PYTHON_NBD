# 5.1.18Ex. (58) – Insert ascending and descending integer values into arrays
a = []
b = []

# range(11) to include 10,
# since range in Python is
# upper-bound exclusive.
for j in range(11):
    a.append(j)
    b.append(10 - j)
print("a =", a)
print("b =", b)
