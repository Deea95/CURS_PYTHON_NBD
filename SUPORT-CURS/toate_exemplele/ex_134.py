# 8.1.10 Ex. (134) – Cascading built-in functions (split, join, length)
a = "----##----------##--------"
Output:
q = "##"
b = len(a)
c = len(a.replace(q, ""))
if c < b:
    print("a contains q")
