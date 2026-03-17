# 10.7.1 Ex. (194) – Return an array with proportions (relative frequencies)
def p(a):                         Output:


max_value = max(a)
n = len(a)
56 %, 11 %, 89 %, 44 %,
m = 100
67 %, 22 %, 100 %, 89 %
# Preallocate the list
# with the required size.
t = [''] * n
for i in range(n):
    t[i] = str(round((m / max_value) * a[i])) + '%'
return t
a = [5, 1, 8, 4, 6, 2, 9, 8]
print(p(a))


# or another version:
def p(a):
    max_value = max(a)
    n = len(a)
    m = 100
    t = []
    for i in range(n):
        t.append(str(round((m / max_value) * a[i])) + '%')
    return t


a = [5, 1, 8, 4, 6, 2, 9, 8]
print(p(a))
