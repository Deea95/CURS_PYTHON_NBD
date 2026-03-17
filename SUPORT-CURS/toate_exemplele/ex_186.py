# 10.4.5 Ex. (186) – Double brute force algorithm (DBFA)
# Double Brute Force Algorithm (DBFA). Output:
def block_allocation(L):          9


a = 1
b = 1
t = 5  # min block length.
m = 8  # max block length.
while True:
    a = a + 1
    t = L % a
    r = L - t
    v = r % 2
    t += 1
    if not (t > 3 and v == 0):
while True:
    m = m + 1
    b = r % m
    if not (b == 0 or m > 1000):
return m
x = block_allocation(133)
print(x)
