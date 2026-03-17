# 10.4.4 Ex. (185) – Pseudo random generator
def prandom(x):           Output:


a = 11
m = 25
0, 17, 4, 11, 13, 10, 2, 14, 21, 23,
c = 17
r = ""
for i in range(10):
    x = (a * x + c) % m
    r += str(x) + ","
return r
# Seed value
x = 3
print(prandom(x))
