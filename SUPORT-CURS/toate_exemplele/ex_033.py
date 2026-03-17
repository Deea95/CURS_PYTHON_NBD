# 4.1.12Ex. (33) – Sum all results of the multiplication between i and j
r = 0

for i in range(10):
    for j in range(10):
        r += j * i
print(r)
