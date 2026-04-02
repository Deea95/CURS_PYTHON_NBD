# # 9.1.1 Ex. (153) – Using an object constructor
# class Obj:
#     def __init__(self, a, b, c, d):
#         self.ax = list(a)
#         self.bx = len(self.ax)
#         self.cx = c - b
#         self.dx = d * c
#
# o1 = Obj("some", 66, 50, 77)
# o2 = Obj("text", 85, 48, 77)
#
# print(o1.ax, "|", o2.ax)
# print(o1.bx, "|", o2.bx)
# print(o1.cx, "|", o2.cx)
# print(o1.dx, "|", o2.dx)
#
# o1.bx = 100
#
# print(o1.bx, "|", o2.bx)
#
#
# # 9.1.5 Ex. (157.ex)
# # facem 3 liste aleatorii si sa instantiem si sa execudam functia dx intr un forloop
# # scriem 3 liste : a1, a2, a3 ( 2 dimensiuni) de aceleasi dimensiune
# import math
# import random
#
# class Obj:
#     def __init__(self):
#         self.AV = 0
#         self.SD = 0
#         self.CV = 0
#
#     def dx(self, a):
#         n = len(a)
#         b = sum(a)
#         x = b / n
#         e = sum([(aj - x) ** 2 for aj in a])
#         s = math.sqrt(e / (n - 1))
#         c = s / x
#
#         self.AV = round(x, 2)
#         self.SD = round(s, 2)
#         self.CV = round(c, 2)
#
# # cream 3 liste bidimensionale (2D), fiecare cu 6 elemente
# a1 = [[random.randint(1, 50) for _ in range(6)] for _ in range(2)]
# a2 = [[random.randint(1, 50) for _ in range(6)] for _ in range(2)]
# a3 = [[random.randint(1, 50) for _ in range(6)] for _ in range(2)]
#
# toate_listele = [a1, a2, a3]
#
# # procesam fiecare sublistă
# for idx, lista2d in enumerate(toate_listele, start=1):
#     print(f"Set {idx}:")
#     for subidx, lst in enumerate(lista2d, start=1):
#         obj = Obj()
#         obj.dx(lst)
#         print(f" Sublista {subidx}: {lst}")
#         print(f"  AV: {obj.AV}, SD: {obj.SD}, CV: {obj.CV}")
#     print("----------------------")
#
# # 159.ex
# import os
#
# # construim calea fișierului în același folder cu scriptul
# file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")
#
# # verificăm dacă fișierul există
# if os.path.exists(file_path):
#     with open(file_path, "r", encoding="utf-8") as f:
#         for line in f:
#             if "ERROR" in line:
#                 print(line.strip())
# else:
#     print(f"Fișierul nu există: {file_path}")
#
#
# # exercitiu
# import os
#
# # Calea fixă către fișier
# file_path = r"C:\Users\CristinaOancea\Desktop\CURS_PYTHON_NBD\SUPORT-CURS\log.txt"
#
# # Verificăm dacă fișierul există
# if os.path.exists(file_path):
#     with open(file_path, "r", encoding="utf-8") as f:
#         for line in f:
#             if "ERROR" in line:
#                 print(line.strip())
# else:
#     print(f"Fișierul nu există: {file_path}")
#
#
# #### transformam in obiecte
# # {"v1": 1, "v2": 52, "v3": 83}
# # {"v1": 19, "v2": 52, "v3": 83}
# # {"v1": 91, "v2": 92, "v3": 83}
#
# import os
# import json
#
# file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")
#
# # Verificăm dacă fișierul există
# if os.path.exists(file_path):
#     with open(file_path, "r", encoding="utf-8") as f:
#         for line in f:
#             if "ERROR" in line:
#                 print(line.strip())
# else:
#     print(f"Fișierul nu există: {file_path}")
#
#
#
#
# import json
#
# txt = '{"v1":["a","b","c"],"v2":' + \
# '[[0,1,0],[1,1,1],[0,1,0]]' + \
# ',"v3":{"c1":["a","b","c"]' + \
# ',"c2":[[0,1,0],[1,1,1],[0' + \
# ',1,0]],"c3":42}}'
# obj = json.loads(txt)
# a = []
# for i in obj['v3']['c1']:
#     a.append(i)
# print(a)
# # sa mutam locatia din v3[c1] la v1 (gen sa luam abc din v1)
# import json
#
# txt = '{"v1":["a","b","c"],"v2":' + \
# '[[0,1,0],[1,1,1],[0,1,0]]' + \
# ',"v3":{"c1":["a","b","c"]' + \
# ',"c2":[[0,1,0],[1,1,1],[0' + \
# ',1,0]],"c3":42}}'
#
# obj = json.loads(txt)
#
# # mutăm valorile din v3[c1] în v1
# obj['v1'] = obj['v3']['c1']
#
# print(obj['v1'])
#
#
#
# # ex cu excel angajati
import os
import csv

# cale fixă către fișier
cale = r"C:\Users\CristinaOancea\Desktop\CRISTINA\Python\CURS_PYTHON_NBD\SUPORT-CURS\angajati.csv"

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

print("Total salarii:", salariu_total)
print("Angajati IT:", angajati_it)
print("Cel mai bine platit:", cel_mai_bine_platit)