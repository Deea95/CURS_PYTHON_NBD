# 10.2.1 Ex. (172) – Function to swap diagonal of matrix
# Function to swap                Output:
# diagonal of matrix.
def swap_diagonal(a):
    n = len(a)
    for i in range(n):
        t = a[i][i]
        a[i][i] = a[i][n - i - 1]
        a[i][n - i - 1] = t

def smc(m):
    r = "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += " " + str(m[i][j]) + " "
        r += "\n"
    return r


a = [
    [3, 1, 2],
    [1, 0, 1],
    [2, 1, 3]
]
swap_diagonal(a)
print(smc(a))
