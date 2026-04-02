# # Replacement for repeat loops with recursion
# # replacement for                  Output:
# # repeat loops.
# def for_loop(a, b, r):
#     a += 1
#     # do stuff from
#     r += 5
#     # to here
#     if a >= b:
#         return r
#     else:
#         return for_loop(a, b, r)
#
# a = for_loop(0, 7, 0)
# print(a)


# # Using an object constructor
# class Obj:
#     def __init__(self, a, b, c, d):   # self se refera la clasa respectiva
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



# # Exercitiu: Construiti o noua clasa care sa scada din valoare lui cx
# # argumentul dat metodei la instantierea obiectului
#
# class Obj:
#     def __init__(self, a, b, c, d,e):
#         self.ex = e
#         self.ax = list(a)
#         self.bx = len(self.ax)
#         self.cx = c - b - self.ex
#         self.dx = d * c
#
# o1 = Obj("some", 66, 50, 77, 1)
# o2 = Obj("text", 85, 48, 77, 2)
#
# print(o1.ax, "|", o2.ax)
# print(o1.bx, "|", o2.bx)
# print(o1.cx, "|", o2.cx)
# print(o1.dx, "|", o2.dx)
# print(o1.ex, "|", o2.ex)
#
# o1.bx = 100
#
# print(o1.bx, "|", o2.bx)

#
# #An object with three properties and a method (I)
# # This example creates an object with three properties.
# # The cx property is a method.
# class Obj:
#     def __init__(self):
#         self.ax = "this"
#         self.bx = "text"
#
#     def cx(self):
#         return self.ax + " " + self.bx
# # Create an instance of the
# # Obj class and call the cx method.
# obj = Obj()
# # print(obj.ax)  # se va afisa primul element
# # print(obj.bx)  # se va afisa al doilea element
# print(obj.cx())


# # An object with three properties and a method (II)
# # This example creates an object with three properties. The cx property is a method.
# class MyObject:
#     def __init__(self):
#         self.ax = "this"
#         self.bx = "text"
#
#     def cx(self, g):  # self denota ca aceasta functie este a obiectului de mai sus
#         t = self.ax + g + str(len(self.bx))
#         return t
# # Create an instance of the class.
#
# obj = MyObject()
#
# # Use the functions and properties of the object.
#
# print(obj.cx("-"))   # "-" este argumentul g din functie cx
# print(obj.ax)
# print(obj.bx)
#
# # Modify the properties.
#
# obj.ax = "super"
# obj.bx = "string"
#
# # Print the modified properties and the result of the function.
#
# print(obj.ax)
# print(obj.bx)
# print(obj.cx("+"))   # "+" este argumentul g din functie cx



# # An object with complex methods
# class Obj:
#     def __init__(self):
#         self.AV = 0
#         self.SD = 0
#         self.CV = 0
#
#     def dx(self, a):
#         n = len(a)
#         b = 0
#         e = 0
#
#         for j in a:
#             b += j
#
#         x = b / n
#
#         for j in a:
#             e += (j - x) ** 2
#
#         s = (e / (n - 1)) ** 0.5
#         c = s / x
#
#         self.AV = x
#         self.SD = s
#         self.CV = c
# # Creating an instance of Obj and applying the dx function.
# obj = Obj()
# a = [5, 6, 2, 9, 44, 200]
# obj.dx(a)
#
# print('AV:', obj.AV)
# print('SD:', obj.SD)
# print('CV:', obj.CV)


# # Instantiati 3 obiecte diferite pentru 3 liste diferite
# # si modificati rezultatele din self.AV, self.SD, self.CV
# # pentru a fi rotunjite la 2 zecimale ( round() are 2 argumente)
#
# class Obj:
#     def __init__(self):
#         self.AV = 0
#         self.SD = 0
#         self.CV = 0
#
#     def dx(self, a):
#         n = len(a)
#         b = 0
#         e = 0
#
#         for j in a:
#             b += j
#
#         x = b / n
#
#         for j in a:
#             e += (j - x) ** 2
#
#         s = (e / (n - 1)) ** 0.5
#         c = s / x
#
#         self.AV = x
#         self.SD = s
#         self.CV = c
#
#         # rotunjire la 2 zecimale
#         self.AV = round(x, 2)
#         self.SD = round(s, 2)
#         self.CV = round(c, 2)
#
# # Creating an instance of Obj and applying the dx function.
# obj = Obj()
#
# # liste
#
# a = [5, 6, 2, 9, 44, 200]
# b= [10, 20, 30, 40, 50]
# c = [3, 7, 8, 12, 15, 18]
#
# # Obiecte diferite
# obj.dx(a)
# obj.dx(b)
# obj.dx(c)
#
#
# print('AV:', obj.AV)
# print('SD:', obj.SD)
# print('CV:', obj.CV)


# # Generate multiple objects with methods using an object constructor and methods.
# import math
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
#
#         e = sum([(aj - x) ** 2 for aj in a])
#         s = math.sqrt(e / (n - 1))
#         c = s / x
#
#         self.AV = x
#         self.SD = s
#         self.CV = c
#
# a = [5, 6, 2, 9, 44, 200]
# b = [7, 4, 6, 8, 6, 4]
#
# box1 = Obj()
# box2 = Obj()
#
# box1.dx(a)
# box2.dx(b)
#
# print('box 1 - AV:', box1.AV)
# print('box 1 - SD:', box1.SD)
# print('box 1 - CV:', box1.CV)
# print('----------------------')
# print('box 2 - AV:', box2.AV)
# print('box 2 - SD:', box2.SD)
# print('box 2 - CV:', box2.CV)


# # adaugati 3 liste (a1, a2, a3) si sa executam functia dx intr-un for loop
#
# import math
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
#
#         e = sum([(aj - x) ** 2 for aj in a])
#         s = math.sqrt(e / (n - 1))
#         c = s / x
#
#         self.AV = x
#         self.SD = s
#         self.CV = c
#
# a1 = [5, 6, 2, 9, 44, 200]
# a2 = [7, 4, 6, 8, 6, 4]
# a3 = [1,2,3,4,5,6]
#
# # obiecte
# boxes = [Obj(), Obj(), Obj()]
#
# # liste grupate
# liste = [a1, a2, a3]
#
# # for loop
# for i in range(3):
#     boxes[i].dx(liste[i])
#
# # afișare
# for i in range(3):
#     print(f'box {i+1} - AV:', boxes[i].AV)
#     print(f'box {i+1} - SD:', boxes[i].SD)
#     print(f'box {i+1} - CV:', boxes[i].CV)
#     print('----------------------')



# # Object to JSON
# # a Python object...
# # ... converted into JSON:
# import json
#
# obj = {"v1": 1, "v2": 2, "v3": 3}
# txt = json.dumps(obj)   # json.dumps(obj) → transforma un obiect → in string
#                         # json.loads(txt) → transforma un  string → in obiect
#
# print(txt)
# # send JSON:
# # print("index.php?obj=" + txt);


# # JSON to Object
# # txt is text received in JSON format.
# # Convert JSON into a Python object:
# # JSON text.
# import json
#
# txt = '{"v1":1,"v2":2,"v3":3}'
# # Parse JSON to create
# # a Python object.
# obj = json.loads(txt)   # json.loads(txt) → transforma un  string → in obiect
#                         # json.dumps(obj) → transforma un obiect → in string
# print(obj['v1'])
# print(obj['v2'])
# print(obj['v3'])



# # Acest exemplu citește un fișier text și afișează doar liniile care conțin "ERROR".
# import os
#
# # construim calea fișierului în același folder cu scriptul
# file_path = r"C:\Users\DanielaOancea\OneDrive - New Business Dimensions\Desktop\NBD\curs Python\log.txt"
#
# # verificăm dacă fișierul există
# if os.path.exists(file_path):
#     with open(file_path, "r", encoding="utf-8") as f:  # encoding="utf-8" - permite citirea diacriticilor
#         for line in f:
#             if "ERROR" in line:
#                 print(line.strip())
# else:
#     print(f"Fișierul nu există: {file_path}")


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




# import json
# import os
#
# # cale către fișier
# file_path = r"C:\Users\AndreeaIote\Desktop\CURS_PYTHON_NBD\SUPORT-CURS\log2.txt"
#
# total_v2 = 0  # accumulator
# count_v2 = 0  # câte valori valide am găsit
#
# if not os.path.exists(file_path):
#     print(f"Fișierul nu există: {file_path}")
# else:
#     with open(file_path, "r", encoding="utf-8") as f:
#         for i, line in enumerate(f, start=1):
#             line = line.strip()
#
#             if not line:
#                 continue
#
#             try:
#                 obj = json.loads(line)
#                 v2_value = obj.get("v2")
#
#                 if isinstance(v2_value, (int, float)):
#                     total_v2 += v2_value
#                     count_v2 += 1
#
#             except json.JSONDecodeError:
#                 print(f"Eroare JSON pe linia {i}: {line}")
#
# print(f"Total v2 = {total_v2}")
# print(f"Număr valori v2 = {count_v2}")



# # Make a matrix from parts of an object
# import json
#
# txt = '{"v1":["a","b","c"],"v2":' + \
#       '[[0,1,0],[1,1,1],[0,1,0]]' + \
#       ',"v3":{"c1":["a","b","c"]' + \
#       ',"c2":[[0,1,0],[1,1,1],[0' + \
#       ',1,0]],"c3":42}}'
#
# obj = json.loads(txt)
# a = []
#
# for i in range(len(obj['v3']['c2'])):
#     a.append([])
#     for j in range(len(obj['v3']['c2'][i])):
#         a[i].append(obj['v3']['c2'][i][j])
#
# def smc(m):
#     r = ''
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             r += str(m[i][j]) + " "
#         r += "\n"
#     return r
#
# print(smc(a))



# # Strings to 1D arrays (I)
# def main_app():
#
#     a = "10|13|55|56|1|3|123"   # pentru fisiere de tip text (cand lucram cu fiesere de tip text de genul)
#     b = "45|33|55|0|1|22|127"
#
#     aa = a.split("|")
#     bb = b.split("|")
#     cc = []
#
#     for i in range(len(aa)):
#         cc.append(daniela(i, aa, bb))
#     print(cc)
#
#
# def daniela(i, aa, bb):
#     return int(aa[i]) * int(bb[len(aa) - 1 - i])
#
# d = main_app()


# # A 2D array loaded from string
# def SMC(matrix):
#
#     result = ""
#     for row in matrix:
#         for item in row:
#             result += item + " "
#         result += "\n"
#     return result
#
# c = 'AAAAA|BBBBB|CCCCC|DDDDD'
# n = c.split('|')
#
# m = [list(row) for row in n]
# print(SMC(m))
# def SMC(matrix):
#
#     result = ""
#     for row in matrix:
#         for item in row:
#             result += item + " "
#         result += "\n"
#     return result
#
# c = 'AAAAA|BBBBB|CCCCC|DDDDD'
# n = c.split('|')
#
# m = [list(row) for row in n]
# print(SMC(m))


# #Load a matrix from a string by using two delimiters
# #Initialize empty lists.
# n = []
# m = []
#
#
# # Input string.
# c = '1,2,4,1,0|3,5,6,7,8|1,2,3,4,5|5,4,3,2,1'
#
# def bahdir(c):
#     # Referencing the
#     # global variable m.
#     global m
#
#     n = c.split('|')
#
#     for i in range(len(n)):
#         m.append(n[i].split(','))
#
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             m[i][j] = int(m[i][j])
#     return m
#
# def smc(m):
#     r = "\n"
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             r += " " + str(m[i][j]) + " "
#         r += "\n"
#     return r
#
# print(smc(bahdir(c)))



# # A function to correctly display a matrix
# def ps(a, s):
#
#     t = ""
#     b = s - (len(str(a)) % s)
#     for i in range(b):
#         t += " "
#     return t
#
# def SMC(m):
#     r = "\n"
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             r += str(m[i][j]) + ps(m[i][j], 3)
#         r += "\n"
#     return r
#
#
# m = [
#     [20, 4, 60],
#     [39, 5, 60],
#     [3, 50, 40]
# ]
# print(SMC(m))



# # A function to load and display matrices
# def load(c):
#     n = c.split('|')
#     m = []
#
#     for i in range(len(n)):
#         m.append(n[i].split(','))
#
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             m[i][j] = int(m[i][j])
#     return m
#
# def SMC(m):
#     r = ""
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             r += str(m[i][j]) + ps(m[i][j],3)
#         r += "\n"
#     return r
#
#
# def ps(a, s):
#     t = ""
#     b = s - (len(str(a)) % s)
#     for i in range(b):
#         t += " "
#     return t
#
#
# c1 = '12,2,44,1,0|34,5,6,7,8|' + \
#      '1,2,3,4,5|5,4,3,2,1'
# c2 = '66,5,45,10,10|37,50,60,17,18|' + \
#      '10,25,37,4,5|5,4,3,2,1'
# c3 = '66,5,45,10,10|37,50,60,17,18|' + \
#      '10,25,37,4,5|5,4,3,2,1'
# print(SMC(load(c1)))
# print(SMC(load(c2)))
# print(SMC(load(c3)))



# import os
# import csv
# cale = r"C:\Users\DanielaOancea\OneDrive - New Business Dimensions\Desktop\NBD\curs Python\CURS_PYTHON_NBD\SUPORT-CURS\angajati.csv"
#
# with open(cale, "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     randuri = list(reader)
#
# angajati_it = []
# salariu_total = 0
# salariu_maxim = -1
# cel_mai_bine_platit = None
#
# for rand in randuri:
#     salariu = int(rand["salariu"])
#     salariu_total += salariu
#
#     # exemplu: filtrăm IT
#     if rand.get("departament") == "IT":
#         angajati_it.append(rand)
#
#     # salariu maxim
#     if salariu > salariu_maxim:
#         salariu_maxim = salariu
#         cel_mai_bine_platit = rand
#
# print("Total salarii:", salariu_total)
# print("Angajati IT:", angajati_it)
# print("Cel mai bine platit:", cel_mai_bine_platit)


# # Load two matrices from strings and make the addition
# def load(c):
#     n = c.split('|')
#     m = []
#     for i in n:
#         m.append([int(x) for x in i.split(',')])
#     return m
#
#
# def SMC(m):
#     r = ""
#     for row in m:
#         for item in row:
#             r += str(item) + ps(item,3)
#         r += "\n"
#     return r
#
#
#
# def ps(a, s):
#     t = ""
#     b = s - (len(str(a)) % s)
#     for _ in range(b):
#         t += " "
#     return(t)
#
#
# c1 = '12,2,44,1,0|34,5,6,7,8|' + \
#     '1,2,3,4,5|5,4,3,2,1'
#
# c2 = '66,5,45,10,10|37,50,60,17,18|' +\
#     '10,25,37,4,5|5,4,3,2,1'
#
# m1 = load(c1)
# m2 = load(c2)
# sm = []
# print(SMC(m1))
# print(SMC(m2))
# for i in range(len(m1)):
#     sm.append([])
#     for j in range(len(m1[i])):
#         sm[i].append(m1[i][j] + m2[i][j])
# print(SMC(sm))
