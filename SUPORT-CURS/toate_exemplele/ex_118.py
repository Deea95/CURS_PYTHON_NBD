a = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
]

b = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
]

# Variante cu pre-alocare
c = [[0] * len(a[0]) for _ in range(len(a))]
r = ""

for i in range(len(a)):
    r += "\n"
    for j in range(len(a[i])):
        c[i][j] = a[i][j] + b[i][j]
        r += str(c[i][j]) + " "

print(r)