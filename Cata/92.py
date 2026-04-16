A = [
    ["a", 88, 146],
    ["b", 34, 124],
    ["c", 96, 564],
    [100, 12, "d"],
]

t = ""

n = len(A)      # rows
m = len(A[0])   # columns

for k in range(n * m):
    j = k % m
    i = k // m

    t += f"{k} A[{i}][{j}]={A[i][j]}\n"

print(t)