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

        self.AV = x
        self.SD = s
        self.CV = c


# generare 3 liste aleatorii
liste = []
for _ in range(3):
    lista = [random.randint(1, 100) for _ in range(6)]
    liste.append(lista)

# creare obiecte + apel dx in loop
obiecte = []

for i, lst in enumerate(liste):
    obj = Obj()
    obj.dx(lst)
    obiecte.append(obj)

    print(f"Lista {i+1}: {lst}")
    print(f"AV: {obj.AV:.2f}")
    print(f"SD: {obj.SD:.2f}")
    print(f"CV: {obj.CV:.2f}")
    print("----------------------")