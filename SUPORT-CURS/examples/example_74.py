a = ["a", "a", "a", "a", "a", "a"]
b = ["b", "b", "b", "b", "b", "b"]
l = len(a) - 1
for k in range(0, l + 1):
    t = a[k]
    a[k] = b[k]
    b[k] = t
print("a =", a)
print("b =", b)
