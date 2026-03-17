# 10.3.6 Ex. (180) – Logical XOR
XOR[0, 0] -> 0


def f_xor(a, b):
    return (a + b) - 2 * (a * b)
    # return (a - b) * (a - b)
    # return ((a + b) * (a + b)) % 2


print('[0, 0] ->', f_xor(0, 0))
