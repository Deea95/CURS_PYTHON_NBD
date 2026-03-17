# 8.2.4 Ex. (139) – Function calls to other functions
def daniela(a, b):
    return a + b

def sebastian(a, b):
    p = daniela(a, b)
    return p


def main_app(x, y):
    cc = sebastian(x, y)
    return cc


d = main_app(66, 100)
print(d)

