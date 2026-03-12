a = 3.1415 # constant
b = 11 # global variable
def compute():
    x = b
    b = compute()
    print(f"{b}\n{A}")