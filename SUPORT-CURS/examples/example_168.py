n = []
m = []
c = '1,2,4,1,0|3,5,6,7,8|1,2,3,4,5|5


def bahdir(c):
    n = c.split('|')
    for i in range(len(n)):
        m.append(n[i].split(','))
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])


def smc(m):
    r = "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += " " + str(m[i][j])
        r += "\n"


print(smc(bahdir(c)))
printing
a
matrix
represented as a
string
of
n
numbers in a
string if necessary.The
code
its
parameter(just
like in the
previous
exam
