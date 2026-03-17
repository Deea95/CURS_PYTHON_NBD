# 5.1.33Ex. (73) – Mix array based on pattern
a = [2, 3, 4, 5, 9, 8, 3]
Output:
b = [1, 2, 3, 4, 5, 6, 7]
c = [0, 1, 1, 0, 0, 0, 1]
c = 1, 3, 4, 4, 5, 6, 3
l = len(a)
for k in range(l):
    if c[k] == 1:
        c[k] = a[k]
    else:
        c[k] = b[k]
print("c =", c)
