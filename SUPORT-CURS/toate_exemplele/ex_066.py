# 5.1.26Ex. (66) – Which is bigger between n and n + 1 ? (optimisation)
a = [2, 3, 4, 5, 9, 8, 3, 8, 3]
l = len(a) - 1
t = ' '
r = '<'

for k in range(0, l):
    if a[k] > a[k + 1]:
        r = ">"
    t += r
    r = "<"
print(t)

