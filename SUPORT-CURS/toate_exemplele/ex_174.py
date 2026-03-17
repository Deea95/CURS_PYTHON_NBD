# 10.2.3 Ex. (174) – Function for rotation of a matrix by 90 degre
# left rotation of a matrix       Output:
# by 90 degree without using
# any extra space.                1 1 1 1
def rev_column(a):                2


0
2
4
n = len(a)
2
3
3
3
m = len(a[0])
for i in range(n):              1
2
2
2
j = 0
1
6
0
3
k = m - 1
1
7
2
3
while j < k:                  1
4
4
3
t = a[j][i]
a[j][i] = a[k][i]
a[k][i] = t
1
4
4
3
j += 1
1
7
2
3
k -= 1
1
6
0
3


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
print(smc(a))
print(smc(a))
