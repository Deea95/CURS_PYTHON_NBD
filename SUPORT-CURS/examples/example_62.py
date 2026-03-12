a = [3, 3, 4, 2, 9, 8, 3]
l = len(a)
min_val = a[0]
for k in range(0, l):
    if a[k] < min_val:
        min_val = a[k]
        print(min_val)