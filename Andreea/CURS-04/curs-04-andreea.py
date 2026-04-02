"""
# 8.3.1 Ex. (146) – Replacement for repeat loops with recursion
# replacement for                  Output:
# repeat loops.
def for_loop(a, b, r):
    a += 1
    # do stuff from
    r += 5
    # to here
    if a >= b:
        return r
    else:
        return for_loop(a, b, r)


a = for_loop(0, 7, 0)
print(a)
"""
# CTRL + s -> se comenteaza tot
"""
# ex 147:
def x(c, s, n):
    s += c
    if len(s) >= n:
        return s[:n]  # ia primii n caractere
    else:
        return x(c, s, n)

a = x("#", "", 10)
print("Repeat:\n[" + a + "]")
"""
"""
# 8.3.3 Ex. (148) – Sum from 0 to n recursively
def sum(n):
    if n <= 1:
        return n

    return n + sum(n - 1)
b = sum(23)
print(f"Sum:[{b}]")
"""
"""
# ex 149:
def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n

c = factorial(10)
print("Factorial:\n[" + str(c) + "]")
"""
"""
# 8.3.5 Ex. (150) – Generate a sequence recursively
def sequence(n, m, i, t):
    m.append(n)
    i += 1
    if i >= t:
        return m
    else:
        return sequence((n - 1) + (n - 2), m, i, t)
    # Testing the function
# and printing the sequence.
d = sequence(5, [], 0, 5)
print("A sequence:\n[", d, "]")
"""
"""
# 8.3.6 Ex. (151) – Generate fibonacci recursively
def fibonacci(n, m, t):
    n += 1
    m.append(m[n - 1] + m[n - 2])

    if n >= t:
        return m
    else:
        return fibonacci(n, m, t)
e = fibonacci(2, [0, 1, 2], 5)
print("Fibonacci:\n[" + ', '.join(map(str, e)) + "]")
"""
"""
# 8.3.7 Ex. (152) – Sum all from array recursively
def sum_array(n, q, r):
    r += q[n]

    if n <= 0:
        return r
    else:
        return sum_array(n - 1, q, r)
q = [1, 3, 3, 4, 5, 9]
f = sum_array(len(q) - 1, q, 0)
print(f"Sum array: [{f}]")
"""
"""
# 9.1.1 Ex. (153) – Using an object constructor
class Obj:
    def __init__(self, a, b, c, d):
        self.ax = list(a)
        self.bx = len(self.ax)
        self.cx = c - b
        self.dx = d * c
        # self - se refera la clasa respectiva

o1 = Obj("some", 66, 50, 77)
o2 = Obj("text", 85, 48, 77)

print(o1.ax, "|", o2.ax)
print(o1.bx, "|", o2.bx)
print(o1.cx, "|", o2.cx)
print(o1.dx, "|", o2.dx)

o1.bx = 100

print(o1.bx, "|", o2.bx)
"""
# ex suplimentar:
# O noua clasa in int lui Obj care sa scada din valoarea lui cx argumentul dat metodei la instantierea obiectului
"""
class Obj:
    def __init__(self, a, b, c, d, e): #__init__ -> nu se modifica!!!!!
        self.ax = list(a)
        self.bx = len(self.ax)
        self.e = e          # întâi definim e
        self.cx = c - b - self.e
        self.dx = d * c

o1 = Obj("some", 66, 50, 77, 1)
o2 = Obj("text", 85, 48, 77, 2)

print(o1.cx, "|", o2.cx)
print( "e: ", o2.e)
"""
"""
# 9.1.2 Ex. (154) – An object with three properties and a method (I)
# This example creates an          Output:
# object with three properties.
# The cx property is a method.     this text
class Obj:
    def __init__(self): # __init__ este ca si main; # functia este default
        self.ax = "this"
        self.bx = "text"

    def cx(self):
        return self.ax + " " + self.bx
    # Create an instance of the
# Obj class and call the cx method.
obj = Obj()
print(obj.ax)
print(obj.cx())
"""
"""
# 9.1.3 Ex. (155) – An object with three properties and a method (II)
# This example creates an object   Output:
# with three properties. The cx
# property is a method.            this-4
class MyObject:
    def __init__(self):
        self.ax = "this"
        self.bx = "text"

    def cx(self, g): # poate sa aiba mai multi parametrii
        t = self.ax + g + str(len(self.bx)) # str(len(self.bx)) = 4
        return t
    # Create an instance
# of the class.

obj = MyObject()

# Use the functions and
# properties of the object.

print(obj.cx("-"))
print(obj.ax)
print(obj.bx)

# Modify the properties.

obj.ax = "super"
obj.bx = "string"

# Print the modified
# properties and the result
# of the function.

print(obj.ax)
print(obj.bx)
print(obj.cx("+"))
"""
"""
# 9.1.4 Ex. (156) – An object with complex methods
class Obj:
    def __init__(self):
        self.AV = 0
        self.SD = 0
        self.CV = 0

    def dx(self, a):
        n = len(a)  # 1️⃣ numarul elementelor
        b = 0
        e = 0

        for j in a:
            b += j  # 2️⃣ suma elementelor

        x = b / n  # 3️⃣ media aritmetica

        for j in a:
            e += (j - x) ** 2  # 4️⃣ suma patratelor abaterilor de la medie

        s = (e / (n - 1)) ** 0.5  # 5️⃣ deviatia standard esantionului
        c = s / x  # 6️⃣ coeficientul de variatie

        self.AV = x
        self.SD = s
        self.CV = c
    # Creating an instance of Obj
# and applying the dx function.
obj = Obj() # seamana cu Object obj = new Object din Java (instantierea clasei)
a = [5, 6, 2, 9, 44, 200]
obj.dx(a)

print('AV:', obj.AV)
print('SD:', obj.SD)
print('CV:', obj.CV)
"""
"""
#instantiati 3 obiecte diferite pentru 3 liste diferite
# si modificati rezultatele din self.av , sd, cv pentru a fi rotunijite
# la 2 zecimale

class Obj:
    def __init__(self):
        self.AV = 0
        self.SD = 0
        self.CV = 0

    def dx(self, a):
        n = len(a)
        b = sum(a)  # suma elementelor
        x = b / n   # media

        e = sum((j - x) ** 2 for j in a)  # suma pătratelor abaterilor
        s = (e / (n - 1)) ** 0.5          # deviația standard
        c = s / x                          # coeficientul de variație

        # salvăm în obiect, rotunjit la 2 zecimale
        self.AV = round(x, 2)
        self.SD = round(s, 2)
        self.CV = round(c, 2)


# 3 liste diferite
list1 = [5, 6, 2, 9, 44, 200]
list2 = [10, 12, 15, 20, 18]
list3 = [1, 2, 3, 4, 5]

# 3 obiecte diferite
obj1 = Obj()
obj2 = Obj()
obj3 = Obj()

obj1.dx(list1)
obj2.dx(list2)
obj3.dx(list3)

print('Obj1 -> AV:', obj1.AV, 'SD:', obj1.SD, 'CV:', obj1.CV)
print('Obj2 -> AV:', obj2.AV, 'SD:', obj2.SD, 'CV:', obj2.CV)
print('Obj3 -> AV:', obj3.AV, 'SD:', obj3.SD, 'CV:', obj3.CV)
"""
"""
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
        s = math.sqrt(e / (n - 1)) # folosim radicalul
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
"""
"""
# facem 3 liste aleatorii si sa instantiem si sa execudam functia dx intr un forloop
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

# generăm 3 liste aleatorii
liste = [
    [random.randint(1, 50) for _ in range(6)],
    [random.randint(1, 50) for _ in range(6)],
    [random.randint(1, 50) for _ in range(6)]
]

# cream si procesam obiectele într-un for loop
obiecte = []
for i, lst in enumerate(liste, start=1):
    obj = Obj()
    obj.dx(lst)
    obiecte.append(obj)
    print(f'Lista {i}: {lst}')
    print(f'AV: {obj.AV}, SD: {obj.SD}, CV: {obj.CV}')
    print('----------------------')
"""
"""
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
"""
"""
# 9.2.1 Ex. (158) – Object to JSON
# a Python object...          Output:
# ... converted into JSON:
import json

obj = {"v1": 1, "v2": 2, "v3": 3} # declaram un dictionar
txt = json.dumps(obj) # convertire un obj in format string

print(txt) # {"v1": 1, "v2": 2, "v3": 3}
print(obj) # {'v1': 1, 'v2': 2, 'v3': 3}
# send JSON:
# print("index.php?obj=" + txt);
"""
"""
# metoda inversa de la ex 158
# 9.2.2 Ex. (159) – JSON to Object
# txt is text received in JSON format. Output:
# Convert JSON into a Python object:
# JSON text.
import json

txt = '{"v1":1,"v2":2,"v3":3}'
# Parse JSON to create
# a Python object.
obj = json.loads(txt) #json in format string
print(obj['v1'])
print(obj['v2'])
print(obj['v3'])
"""
"""
import os

# Calea fixă către fișier
     # se ia de mai jos !!!!!!! da eroare la compilare!!!1
# Verificăm dacă fișierul există
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "ERROR" in line:
                print(line.strip())
else:
    print(f"Fișierul nu există: {file_path}")
"""
"""
import json
import os

# cale către fișier


# verificăm dacă există fișierul
if not os.path.exists(file_path):
    print(f"Fișierul nu există: {file_path}")
else:
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()

            # sărim peste linii goale
            if not line:
                continue

            try:
                obj = json.loads(line)

                # afișare completă
                #print(f"Linia {i}: {obj}")

                # exemplu: acces câmpuri (dacă există)
                print(obj.get("v2"))

            except json.JSONDecodeError:
                print(f"Eroare JSON pe linia {i}: {line}")
"""
"""
import json
import os

# cale către fisier
file_path = r"C:UsersAndreeaIoteDesktopCURS_PYTHON_NBDSUPORT-CURSlog2.txt"

total_v2 = 0  # accumulator
count_v2 = 0  # cate valori valide am gasit

if not os.path.exists(file_path):
    print(f"Fisierul nu exista: {file_path}")
else:
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                obj = json.loads(line)
                v2_value = obj.get("v2")

                if isinstance(v2_value, (int, float)):
                    total_v2 += v2_value
                    count_v2 += 1

            except json.JSONDecodeError:
                print(f"Eroare JSON pe linia {i}: {line}")

print(f"Total v2 = {total_v2}")
print(f"Numar valori v2 = {count_v2}")
"""
"""
import json

txt = '{"v1":["a","b","c"],"v2":' + \
'[[0,1,0],[1,1,1],[0,1,0]]' + \
',"v3":{"c1":["a","b","c"]' + \
',"c2":[[0,1,0],[1,1,1],[0' + \
',1,0]],"c3":42}}'
obj = json.loads(txt)
a = []
for i in obj['v3']['c1']:
    a.append(i)
print(a)
# sa mutam locatia din v3[c1] la v1 (gen sa luam abc din v1)
"""
"""
import json

txt = '{"v1":["a","b","c"],"v2":' + \
'[[0,1,0],[1,1,1],[0,1,0]]' + \
',"v3":{"c1":["a","b","c"]' + \
',"c2":[[0,1,0],[1,1,1],[0' + \
',1,0]],"c3":42}}'

obj = json.loads(txt)

# mutăm valorile din v3[c1] în v1
obj['v1'] = obj['v3']['c1']

print(obj['v1'])
"""
"""
import os
import csv

# cale fixă către fișier
cale = r"C:\\Users\\AndreeaIote\\Desktop\\CURS_PYTHON_NBD\\SUPORT-CURS\\angajati.csv"

with open(cale, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    randuri = list(reader)

angajati_it = []
salariu_total = 0
salariu_maxim = -1
cel_mai_bine_platit = None

for rand in randuri:
    salariu = int(rand["salariu"])
    salariu_total += salariu

    # exemplu: filtrăm IT
    if rand.get("departament") == "IT":
        angajati_it.append(rand)

    # salariu maxim
    if salariu > salariu_maxim:
        salariu_maxim = salariu
        cel_mai_bine_platit = rand
print("Angajati IT:")
for ang in angajati_it:
    print(ang["nume"], ang["salariu"])

print("Total salarii:", salariu_total)
print("Angajati IT:", angajati_it)
print("Cel mai bine platit:", cel_mai_bine_platit)

print("Salariu mediu: ", salariu_total/len(randuri))
print("Salariu maxim: ", cel_mai_bine_platit["nume"],salariu_maxim)
"""

# 10.1.7 Ex. (171) – Load two matrices from strings and make the addition
def load(c):
    n = c.split('|')
    m = []

    for i in n:
        m.append([int(x) for x in i.split(',')])
    return m

def SMC(m):
    r = ""
    for row in m:
        for item in row:
            r += str(item) + ps(item, 3)
        r += "\n"
    return r

def ps(a, s):
    t = ""
    b = s - (len(str(a)) % s)
    for _ in range(b):
        t += " "
    return t


c1 = '12,2,44,1,0|34,5,6,7,8|' + \
     '1,2,3,4,5|5,4,3,2,1'
c2 = '66,5,45,10,10|37,50,60,17,18|' + \
     '10,25,37,4,5|5,4,3,2,1'

m1 = load(c1)
m2 = load(c2)

sm = []

print(SMC(m1))
print(SMC(m2))

for i in range(len(m1)):
    sm.append([])
    for j in range(len(m1[i])):
        sm[i].append(m1[i][j] + m2[i][j])
print(SMC(sm))
