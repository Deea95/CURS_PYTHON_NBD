# 10.4.4 Ex. (185) – Pseudo random generator
def prandom(x):

    a = 11
    m = 25
    c = 17
    r = ""
    for i in range(10):
        x = (a * x + c) % m
        r += str(x) + ","
    return r
# Seed value
x = 3
print(prandom(x))
