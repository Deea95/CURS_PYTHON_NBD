# 10.3.4 Ex. (178) – Logical NAND (NOT AND)

def f_nand(a, b):
    return f_not(f_and(a, b))


def f_not(a):
    return 1 - a

def f_and(a, b):
    return a * b

print('[1, 1] -> ' + str(f_nand(1, 1)))
