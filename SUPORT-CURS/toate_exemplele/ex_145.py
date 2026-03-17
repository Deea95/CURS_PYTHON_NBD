a = 16

def f(x):
    return x + x / x - x * x

def p():
    global b
    x = a - 11
    b = x + x / x - x * x
    b = f(a)
    print(b)

p()
print(b)