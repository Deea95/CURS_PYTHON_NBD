# 10.4.3 Ex. (184) – Greatest common divisor (GCD)
# greatest common divisor (GCD).  Output:
def gcd(a, b):
    if a == 0:
        return b
    while b != 0:
        if a > b:
         a -= b
        else:
         b -= a
    return a
print(gcd(45, 12))
