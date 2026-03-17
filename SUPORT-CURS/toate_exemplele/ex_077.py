# 5.1.37Ex. (77) – The welding of array values
# intermitent melting     Output:
a = [1, 2, 3, 4, 5, 6, 7]
a = 1, 4, 3, 6, 5, 8, 7
b = [2, 2, 2, 2, 2, 2, 2]
b = 2, 4, 2, 6, 2, 8, 2
l = len(a) - 1
k = 0
while k < l:
    k += 1
    a[k] = a[k] + b[k]
    b[k] = a[k]
    k += 1
print("a =", a)
print("b =", b)
