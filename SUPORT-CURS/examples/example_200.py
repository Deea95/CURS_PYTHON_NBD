# txt to hex.
a = ".~ text"
b = ''
c = [None] * len(a)
for i in range(len(a)):
    b = format(ord(a[i]), 'x')
    # if len(b) < 2:
        # c[i] = "0" + b
        # else:
            # c[i] = b
            print(c)