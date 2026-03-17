# 5.1.35Ex. (75) – Intermittent value swap
# ziperr - intermittent value swap Output:
a = ["a", "a", "a", "a", "a", "a"]
a = a, b, a, b, a, b, a,
b = ["b", "b", "b", "b", "b", "b"]
b = b, a, b, a, b, a, b,
l = len(a) - 1
k = 0
while k <= l:
    k += 1
    t = a[k]
    a[k] = b[k]
    b[k] = t
    k += 1
print("a =", a)
print("b =", b)
