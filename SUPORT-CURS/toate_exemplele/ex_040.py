# 4.1.19Ex. (40) – One for loop that simulates two for loops
i = j = 0
Output:
n1 = 2
n2 = 3
i = 0, j = 0
q = n1 * n2
i = 0, j = 1
i = 0, j = 2
for v in range(q):
    i = 1, j = 0
j = v % n2
i = 1, j = 1
if j == 0 and v != 0 and i < n1 and v != q: i = 1, j = 2
i += 1
print(f"i = {i}, j = {j}")
