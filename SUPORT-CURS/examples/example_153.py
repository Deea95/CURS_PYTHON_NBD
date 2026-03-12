def __init__(self, a, b, c, d):
    self.ax = list(a)
    self.bx = len(self.ax)
    self.cx = c - b
    self.dx = d * c


o1 = Obj("some", 66, 50, 77)
o2 = Obj("text", 85, 48, 77)
print(o1.ax, "|", o2.ax)
print(o1.bx, "|", o2.bx)
print(o1.cx, "|", o2.cx)
print(o1.dx, "|", o2.dx)
o1.bx = 100
print(o1.bx, "|", o2.bx)
and o2
are
printed
side
by
side
for comparis
    is modified
    to
    100, and its
    new
    value is print
