# 4.1.16Ex. (37) – Nested for loops & summation based on counters and upper limits (II)
a = 0
m = 4
for j in range(1, m + 1):
    for i in range(1, j + 1):
        a = a + (i+ j * m)
print(a)
