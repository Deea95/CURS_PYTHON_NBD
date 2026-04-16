# 9.1.1 Ex. (153) – Using an object constructor
class cata:
    def __init__(self, a, b, c, d,e):
        self.px = e
        self.ax = list(a)
        self.bx = len(self.ax)
        self.cx = c - b - self.px
        self.dx = d * c

o1 = cata("some", 66, 50, 77,1)
o2 = cata("text", 85, 48, 77,2)

print(o1.ax, "|", o2.ax)
print(o1.bx, "|", o2.bx)
print(o1.cx, "|", o2.cx)
print(o1.dx, "|", o2.dx)

o1.bx = 100

print(o1.bx, "|", o2.bx)
