# 10.3.3 Ex. (177) – Logical OR
OR[1, 0] -> 1


def f_or(a, b):
    return (a + b) - (a * b)


print(f'[1, 0] -> {f_or(1, 0)}')
