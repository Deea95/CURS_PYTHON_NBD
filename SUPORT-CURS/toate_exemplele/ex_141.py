# 8.2.6 Ex. (141) – Function chaining - nested function calls
def c(x):                          Output:


return x + x / x - x * x
a = 3
b = c(c(c(c(a))))
b = -b
print(b)
