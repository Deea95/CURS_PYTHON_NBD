# 5.1.27Ex. (67) – Sum two arrays
a = [2, 3, 4, 5, 9, 8, 3]
Output:
b = [1, 2, 3, 4, 5, 6, 7]
c = []
c = 3, 5, 7, 9, 14, 14, 10
l = len(a) - 1
for k in range(l + 1):
    c.append(a[k] + b[k])
print("c =", c)
