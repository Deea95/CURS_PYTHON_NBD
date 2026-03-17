# 10.8.1 Ex. (200) – Text (txt) to hexadecimal (hex)
# txt to hex.                  Output:
a = ".~ text"
2
e, 7
e, 20, 74, 65, 78, 74
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
