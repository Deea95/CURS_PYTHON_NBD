# 10.2.2 Ex. (173) – Function to transpose a matrix
# Function to transpose a matrix. Output:
def transpose(a):                 1


5
9
4
n = len(a)
2
6
0
5
m = len(a[0])
3
7
2
6
for i in range(n):
    for j in range(i, m):
        t = a[j][i]
        a[j][i] = a[i][j]  # swap.
        a[i][j] = t


def smc(m):
    r = "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += " " + str(m[i][j]) + " "
        r += "\n"
    return r


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 2, 3],
    [4, 5, 6, 7]
]
print(smc(a))
