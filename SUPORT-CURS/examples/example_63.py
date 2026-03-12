a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
l = len(a)
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
the
value
at
index
k in array
a(a[k]) is great
and if so, updates maxA to this new maximu
index
k in array
b(b[k]) is greater
than
the
c
b.Thus, this
code
finds and prints
the
maxi
5
Dynamically
Resizable
Arrays(Lists)
