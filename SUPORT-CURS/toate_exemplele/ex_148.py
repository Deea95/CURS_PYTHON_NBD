# Sum from 0 to n recursively
def sum(n):
    if n <= 1:
        return n

    return n + sum(n - 1)
b = sum(23)
print(f"Sum:[{b}]")
