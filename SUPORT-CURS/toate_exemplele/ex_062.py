# 5.1.22Ex. (62) – Min value from array
a = [3, 3, 4, 2, 9, 8, 3]
Output:
l = len(a)
min_val = a[0]
for k in range(0, l):
    if a[k] < min_val:
        min_val = a[k]
print(min_val)
In
the
above
code, there is an
array
a
initialized
with values, namely[3, 3, 4, 2, 9, 8, 3].
