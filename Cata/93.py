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
    i = (k - j) // m

    t += str(k) + " A[" + str(i) + "][" + str(j) + "]="
    t += str(A[i][j]) + "\n"

print(t)