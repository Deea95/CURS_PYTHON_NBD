# 10.8.3 Ex. (202) – A txt to hex with in-place replacement
# txt to hex by replacing each character with Output:
# the hex code in the same element of the array
a = list(".~ text")
for i in range(len(a)):
    a[i] = format(ord(a[i]), 'x')
    a[i] = a[i] if len(a[i]) >= 2 else "0" + a[i]
print(a)
