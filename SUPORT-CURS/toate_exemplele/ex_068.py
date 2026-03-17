# 5.1.28Ex. (68) – Simple array mapping
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Output:
b = [1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1]
c = []
c = 9, 9, 9, 8, 8, 8, 9, 9, 9, 9, 9
for j in range(11):
    c.append(a[b[j]])
print("c =", c)
