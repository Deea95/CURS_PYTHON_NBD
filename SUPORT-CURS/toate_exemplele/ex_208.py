# 11.1.2 Ex. (208) – Logic gate functions applied to matrix elements
def f_not(a):                     Output:


return 1 - a


def f_and(a, b):                  0


1
0
return a * b
1
1
1


def f_or(a, b):
    return (a + b) - (a * b)


def f_nand(a, b):
    return f_not(f_and(a, b))


def f_nor(a, b):
    return f_not(f_or(a, b))


def f_xor(a, b):
    return (a + b) - 2 * (a * b)


def f_xnor(a, b):
    return f_not(f_xor(a, b))


a = [
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 0]
]
b = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]
c = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
n = len(a)
m = len(a[0])
r = ''
for i in range(n):
    r += '\n'
    for j in range(m):
        c[i][j] = f
        _xnor(a[i][j], b[i][j])
        r += str(c[i][j]) + " "
print(r)
