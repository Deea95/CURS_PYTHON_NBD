class Obj:
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

        # rotunjire la 2 zecimale
        self.AV = round(x, 2)
        self.SD = round(s, 2)
        self.CV = round(c, 2)


# liste diferite
a1 = [5, 6, 2, 9, 44, 200]
a2 = [10, 20, 30, 40, 50]
a3 = [3, 7, 7, 19, 24, 35]

# obiecte diferite
obj1 = Obj()
obj2 = Obj()
obj3 = Obj()

# apeluri
obj1.dx(a1)
obj2.dx(a2)
obj3.dx(a3)

# rezultate
print("Obj1 -> AV:", obj1.AV, "SD:", obj1.SD, "CV:", obj1.CV)
print("Obj2 -> AV:", obj2.AV, "SD:", obj2.SD, "CV:", obj2.CV)
print("Obj3 -> AV:", obj3.AV, "SD:", obj3.SD, "CV:", obj3.CV)