# 5.1.20Ex. (60) – Pointless equilibrium
a = []
Output:
l = 10
a = 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
for j in range(l + 1):
    a.append(j + (l - j))
print(a)
# or a second version:
l = 10
# Initialize a list
# of length l+1.
a = [None] * (l + 1)
for j in range(l + 1):
    a[j] = j + (l - j)
print(a)
