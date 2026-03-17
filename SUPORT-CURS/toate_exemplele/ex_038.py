# 4.1.17Ex. (38) – Nested for loops & summation based on counters and upper limits (III)
a = 0
Output:
m = 5
n = 7
445
for j in range(1, m + 1):
    for i in range(j, n + 1):
        a += (i + j * m)
print(a)
