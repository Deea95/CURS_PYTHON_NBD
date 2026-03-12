def sum(n):
    if n <= 1:
        return n + sum(n - 1)


b = sum(23)
print(f"Sum:[{b}]")
“Sum: [” with the value of b, and then adding
