# 5.1.27Ex. (67) – Sum two arrays
a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = []

l = len(a) - 1
for k in range(l + 1):
    c.append(a[k] + b[k])
print("c =", c)
