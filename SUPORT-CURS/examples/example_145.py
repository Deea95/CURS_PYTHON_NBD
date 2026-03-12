a = 16
def f(x):
    def p():
        x = a - 11
        b = x + x / x - x * x
        b = f(a)
        print(b)
        print(b)