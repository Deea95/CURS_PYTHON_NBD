# 9.1.1 Ex. (153) – Using an object constructor
class Obj:
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


# Construiti o clasa in interiorul clasei Obj care sa scada din valoarea lui cx
# argumentul dat metodei la instantierea obiectului

class Obj:
    def __init__(self, a, b, c, d,e):
        self.paul = e
        self.ax = list(a)
        self.bx = len(self.ax)
        self.cx = c - b - self.paul
        self.dx = d * c


o1 = Obj("some", 66, 50, 77, 1)
o2 = Obj("text", 85, 48, 77, 2)

print(o1.paul)
print(o2.paul)
print(o1.ax, "|", o2.ax)
print(o1.bx, "|", o2.bx)
print(o1.cx, "|", o2.cx)
print(o1.dx, "|", o2.dx)


o1.bx = 100

print(o1.bx, "|", o2.bx)