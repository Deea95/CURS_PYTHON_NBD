def x(c, s, n):
    s += c
    if len(s) >= n:
    else:
        return x(c, s, n)


a = x("#", "", 10)
print("Repeat:\n[" + a + "]")
