# 9.1.5 Ex. (157) – Generate multiple objects with methods
# Using an object            Output:
# constructor and methods.
import math

class Obj:
    def __init__(self):
        self.AV = 0
        self.SD = 0
        self.CV = 0

    def dx(self, a):
        n = len(a)
        b = sum(a)
        x = b / n

        e = sum([(aj - x) ** 2 for aj in a])
        s = math.sqrt(e / (n - 1))
        c = s / x

        self.AV = x
        self.SD = s
        self.CV = c

a = [5, 6, 2, 9, 44, 200]
b = [7, 4, 6, 8, 6, 4]

box1 = Obj()
box2 = Obj()

box1.dx(a)
box2.dx(b)

print('box 1 - AV:', box1.AV)
print('box 1 - SD:', box1.SD)
print('box 1 - CV:', box1.CV)
print('----------------------')
print('box 2 - AV:', box2.AV)
print('box 2 - SD:', box2.SD)
print('box 2 - CV:', box2.CV)


# 9.1.5 Ex. (157.ex)
# facem 3 liste aleatorii si sa instantiem si sa execudam functia dx intr un forloop
# scriem 3 liste : a1, a2, a3 ( 2 dimensiuni) de aceleasi dimensiune
import math
import random

class Obj:
    def __init__(self):
        self.AV = 0
        self.SD = 0
        self.CV = 0

    def dx(self, a):
        n = len(a)
        b = sum(a)
        x = b / n
        e = sum([(aj - x) ** 2 for aj in a])
        s = math.sqrt(e / (n - 1))
        c = s / x

        self.AV = round(x, 2)
        self.SD = round(s, 2)
        self.CV = round(c, 2)

# cream 3 liste bidimensionale (2D), fiecare cu 6 elemente
a1 = [[random.randint(1, 50) for _ in range(6)] for _ in range(2)]
a2 = [[random.randint(1, 50) for _ in range(6)] for _ in range(2)]
a3 = [[random.randint(1, 50) for _ in range(6)] for _ in range(2)]

toate_listele = [a1, a2, a3]

# procesam fiecare sublistă
for idx, lista2d in enumerate(toate_listele, start=1):
    print(f"Set {idx}:")
    for subidx, lst in enumerate(lista2d, start=1):
        obj = Obj()
        obj.dx(lst)
        print(f" Sublista {subidx}: {lst}")
        print(f"  AV: {obj.AV}, SD: {obj.SD}, CV: {obj.CV}")
    print("----------------------")