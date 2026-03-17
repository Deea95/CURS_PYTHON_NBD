# 5.1.21Ex. (61) – Max value from array
a = [2, 3, 4, 5, 9, 8, 3]
Output:
l = len(a)
max_val = 0
for k in range(l):
    if a[k] > max_val:
        max_val = a[k]
print(max_val)
