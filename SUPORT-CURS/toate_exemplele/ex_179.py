# 10.3.5 Ex. (179) – Logical NOR (NOT OR)
NOR[0, 0] -> 1


def f_nor(a, b):
    return f_not(f_or(a, b))


def f_not(a):
    return 1 - a


def f_or(a, b):
    return (a + b) - (a * b)


result = f_nor(0, 0)
print(f'[0, 0] -> {result}')
