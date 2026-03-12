def __init__(self):
    self.AV = 0
    self.SD = 0
    self.CV = 0


def dx(self, a):
    n = len(a)
    b = 0
    e = 0
    for j in a:
        b += j
    x = b / n
    for j in a:
        e += (j - x) ** 2
    s = (e / (n - 1)) ** 0.5
    c = s / x
    self.AV = x
    self.SD = s
    self.CV = c


obj = Obj()
a = [5, 6, 2, 9, 44, 200]
obj.dx(a)
print('AV:', obj.AV)
print('SD:', obj.SD)
print('CV:', obj.CV)
loop, the
mean(average)
x is calculated
by
di
by(n − 1).The
coefficient
of
variation
c is
calculation, there
are
three
print
statements
t
the
print
function
to
output
the
mean(AV),
variation(CV)
to
the
console.Note
that
varia
square
root
of
the
variance.The
expression(e
× q0
.5 = q0
.5 + 0.5 = q1 = q, where
q is a
nu
