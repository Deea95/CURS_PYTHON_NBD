a = 3.1415  # constant
b = 11      # global variable

def compute():
    x = b
    return x + x / x - x * x

b = compute()

print(f"{b}\n{a}")