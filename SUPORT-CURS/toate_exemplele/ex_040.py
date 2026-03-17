# 4.1.19Ex. (40) – One for loop that simulates two for loops
i = j = 0
n1 = 2
n2 = 3
q = n1 * n2

for v in range(q):
    j = v % n2
    if j == 0 and v!= 0 and i < n1 and v != q:
        i += 1
    print(f"i = {i}, j = {j}")
