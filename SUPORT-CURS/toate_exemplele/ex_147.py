# 8.3.2 Ex. (147) – Repeat string n times recursively
def x(c, s, n):                    Output:


s += c
if len(s) >= n:                 Repeat:
return s[  ##########]
else:
return x(c, s, n)
a = x("#", "", 10)
print("Repeat:\n[" + a + "]")
