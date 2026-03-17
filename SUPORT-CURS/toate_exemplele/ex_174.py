# 10.2.3 Ex. (174) – Function for rotation of a matrix by 90 degre
# left rotation of a matrix       Output:
# by 90 degree without using
# any extra space.                1 1 1 1
def rev_column(a):
    n = len(a)
    m = len(a[0])
    for i in range(n):
        j = 0
        k = m - 1
        while j < k:
            t = a[j][i]
            a[j][i] = a[k][i]
            a[k][i] = t
            j += 1
            k -= 1

def transpose(a):
    n = len(a)
    m = len(a[0])
    for i in range(n):
        for j in range(i, m):
            t = a[j][i]
            a[j][i] = a[i][j]
            a[i][j] = t


def smc(m):
    r = "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += " " + str(m[i][j]) + " "
        r += "\n"
    return r

a = [
    [1, 1, 1, 1],
    [2, 6, 7, 4],
    [2, 0, 2, 4],
    [2, 3, 3, 3]
]
print(smc(a))
transpose(a)
print(smc(a))
rev_column(a)
print(smc(a))
