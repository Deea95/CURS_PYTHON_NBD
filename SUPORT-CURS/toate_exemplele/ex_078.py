# 5.1.38Ex. (78) – Static modulo-fill up array with modulo results
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Output:
b = []
c = 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0
for j in range(11):
    b.append(a[j] % 3)
print("c =", b)
