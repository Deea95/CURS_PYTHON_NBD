# 8.3.3 Ex. (148) – Sum from 0 to n recursively
def sum(n):                        Output:


if n <= 1:
    return n
    Sum: [276]
return n + sum(n - 1)
b = sum(23)
print(f"Sum:[{b}]")
