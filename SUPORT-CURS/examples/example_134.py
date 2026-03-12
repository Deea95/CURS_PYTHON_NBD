a = "----##----------##--------"
q = "##"
b = len(a)
c = len(a.replace(q, ""))
if c < b:
    print("a contains q")