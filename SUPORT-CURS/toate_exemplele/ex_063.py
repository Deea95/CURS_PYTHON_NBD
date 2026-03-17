# 5.1.23Ex. (63) – Max value above two arrays of the same size
a = [2, 3, 4, 5, 9, 8, 3]
Output:
b = [1, 2, 3, 4, 5, 6, 7]
l = len(a)
9
max_value = 0
max_a = 0
max_b = 0
for k in range(l):
    if a[k] > max_a:
        max_a = a[k]
    if b[k] > max_b:
        max_b = b[k]
    if max_a > max_value:
        max_value = max_a
    if max_b > max_value:
        max_value = max_b
print(max_value)
