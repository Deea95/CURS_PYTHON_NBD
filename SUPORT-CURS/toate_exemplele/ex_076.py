# 5.1.36Ex. (76) – Reverse string
# a = 'abcdef'                     Output:
# b = list(a)
b = ['a', 'b', 'c', 'd', 'e', 'f']
n = len(b)
c = [None] * n
for i in range(n):
    c[i] = b[n - i - 1]
print(c)
