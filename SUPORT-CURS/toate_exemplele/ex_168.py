# 10.1.4 Ex. (168) – Load a matrix from a string by using two delimiters
# Initialize empty lists.         Output:
n = []
m = []
1
2
4
1
0
# Input string.                   1 2 3 4 5
c = '1,2,4,1,0|3,5,6,7,8|1,2,3,4,5|5,4,3,2,1'
5
4
3
2
1


def bahdir(c):
    # Referencing the
    # global variable m.
    n = c.split('|')
    for i in range(len(n)):
        m.append(n[i].split(','))
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m


def smc(m):
    r = "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += " " + str(m[i][j]) + " "
        r += "\n"
    return r


print(smc(bahdir(c)))
This
implementation
defines
a
series
of
variables and functions
for manipulating and
