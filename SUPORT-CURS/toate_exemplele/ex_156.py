# 9.1.4 Ex. (156) – An object with complex methods
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

        self.AV = x
        self.SD = s
        self.CV = c
    # Creating an instance of Obj
# and applying the dx function.
obj = Obj()
a = [5, 6, 2, 9, 44, 200]
obj.dx(a)

print('AV:', obj.AV)
print('SD:', obj.SD)
print('CV:', obj.CV)
