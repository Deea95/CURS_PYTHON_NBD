# 5.1.29Ex. (69) – Sum by coordinates (I)
a = [2, 3, 4, 5, 9, 8, 3]
Output:
b = [1, 2, 3, 4, 5, 6, 7]
c = [1, 1, 1, 4, 4, 4, 6]
c = 4, 5, 6, 13, 14, 15, 10
l = len(a) - 1
for k in range(0, l + 1):
    c[k] = a[c[k]] + b[k]
print("c =", c)
