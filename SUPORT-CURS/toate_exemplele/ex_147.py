def x(c, s, n):
    s += c
    if len(s) >= n:
        return s[:n]  # ia primii n caractere
    else:
        return x(c, s, n)

a = x("#", "", 10)
print("Repeat:\n[" + a + "]")