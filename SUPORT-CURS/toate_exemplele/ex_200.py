# 10.8.1 Ex. (200) – Text (txt) to hexadecimal (hex)
# txt to hex.
a = ".~ text"
b = ''
c = [None] * len(a)

for i in range(len(a)):
    b = format(ord(a[i]), 'x')
    c[i] = "0" + b if len(b) < 2 else b
    # if len(b) < 2:
    #  c[i] = "0" + b
    # else:
    #  c[i] = b
print(c)
