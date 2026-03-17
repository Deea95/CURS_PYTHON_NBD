# 8.2.8 Ex. (143) – Global vaiables and constants
a = 3.1415  # constant              Output:
b = 11  # global variable          -109


def compute():
    x = b
    return x + x / x - x * x


b = compute()
print(f"{b}\n{A}")
