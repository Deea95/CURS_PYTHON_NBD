# 5.1.25Ex. (65) – Which is bigger between n and n + 1?
a = [2, 3, 4, 5, 9, 8, 3, 8, 3]

l = len(a) - 1
t = ''
for k in range(l):
    if a[k] > a[k + 1]:
        t += '>'
    else:
        t += '<'
print(t)
