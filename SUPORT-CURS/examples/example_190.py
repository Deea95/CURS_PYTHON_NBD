a = {}
b = [3, 6, 2, 78, 99, 1, 4]
n = len(b)
r = n
for i in range(n):
    a[b[i]] = b[i]
m = max(a.keys())
for j in range(m, 0, -1):
    if j in a:
        b[n - r] = a[j]
        r -= 1
print(b)

