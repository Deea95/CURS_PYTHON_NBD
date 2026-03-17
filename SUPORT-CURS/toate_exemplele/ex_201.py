# 10.8.2 Ex. (201) – A txt to hex from array a to array b
# txt to hex from array a to   Output:
# array b element corespondence
a = list(".~ text")
b = [None] * len(a)
for i in range(len(a)):
    b[i] = format(ord(a[i]), 'x')
    b[i] = b[i] if len(b[i]) >= 2 else "0" + b[i]
print(b)
