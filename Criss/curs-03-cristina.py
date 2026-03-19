"""Se da vectorul a = [9,9,9,9,9,1,1,1,1,1]
1. Incrementati valorile din ultimele 6 elemente ale lui a.
   raspuns: [9,9,9,9,10,2,2,2,2]"""

# var 1
a = [9, 9, 9, 9, 9, 1, 1, 1, 1, 1]

for i in range(len(a) - 6, len(a)):
    a[i] += 1

print(a)

# var 2
"""a=[9,9,9,9,9,1,1,1,1,1]

b=len(a)

for r in range(b):
    if r>=b-6:
       a[r]=a[r]+1

print (a) """

""" 2. a= [9,9,9,9,10,2,2,2,2]
   Introduceti in primele 5 elemente valorile complementare ale valorilor existente.
   raspuns: a =[1,1,1,1,0,2,2,2,2,2]"""

a = [9, 9, 9, 9, 9, 1, 1, 1, 1, 1]

m = len(a)

for i in range(m - 6, m):
    a[i] += 1

print(a)

for i in range(5):
    a[i] = 10 - a[i]

print(a)

""" 3. a= [1,1,1,1,0,2,2,2,2,2]
   Faceti un schimb de valori intre primul si ultimul element (swap).
   raspuns: a =[2,1,1,1,0,2,2,2,2,1]"""
#var 1
a = [1,1,1,1,0,2,2,2,2,2]

# swap
a[0], a[-1] = a[-1], a[0]

print(a)

#var 2
a=[1,1,1,1,0,2,2,2,2,2]
t=""

for i in range(5):
    t=a[0]
    a[0]=a[9]
    a[9]=t

print(a)


""" Se da matricea binara:
a=[[1,1,5,5,5],
  [0,1,0,5,1],
  [1,0,3,1,1],
  [0,0,0,3,3],
  [1,0,1,3,1]]
  Identificati valorile unice din matricea a si aratati frecventa fiecareia dintre ele."""

a = [[1,1,5,5,5],
     [0,1,0,5,1],
     [1,0,3,1,1],
     [0,0,0,3,3],
     [1,0,1,3,1]]

frecventa = {}

for linie in a:
    for elem in linie:
        if elem in frecventa:
            frecventa[elem] += 1
        else:
            frecventa[elem] = 1

print(frecventa)


""" Se dau matricile:
m = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
    ]

t = [
    [1, 1, 1],
    [3, 5, 6],
    [3, 5, 4]
    ]
  Faceti suma intre elementele omolog si stocati rezultatul intr-o matrice c."""

m = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
    ]

t = [
    [1, 1, 1],
    [3, 5, 6],
    [3, 5, 4]
    ]

c = []

for i in range(len(m)):
    linie = []
    for j in range(len(m[i])):
        linie.append(m[i][j] + t[i][j])
    c.append(linie)

# Afișare pe linii separate
for linie in c:
    print(linie)


"""Se da matricea binara:
q=[
[1,1,1],
[0,0,0],
[0,0,1]
]
Folositi matricea q ca harta pt operatii. 
Anume, valoarea 1 din q trebuie sa duca la sumarea valorilor din elementele omolog ale lui m si t,
iar valoarea 0 din q trebuie sa duca la o inmultire cu un scalar s = 3, ale elementului omolog din t"""

m = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
]

t = [
    [1, 1, 1],
    [3, 5, 6],
    [3, 5, 4]
]

q = [
    [1, 1, 1],
    [0, 0, 0],
    [0, 0, 1]
]

s = 3
c = []

for i in range(len(q)):
    linie = []
    for j in range(len(q[i])):
        if q[i][j] == 1:
            # q = 1 → sumă între m și t
            linie.append(m[i][j] + t[i][j])
        else:
            # q = 0 → înmulțire cu scalarul s a elementului din t
            linie.append(t[i][j] * s)
    c.append(linie)

# Afișare pe linii
for linie in c:
    print(linie)


""" Se dau matricile: 
a= [
    [2, 4, 4],
    [3, 5, 6],
    [1, 5, 4]
]

b= [
    [2, 4, 4],
    [3, 9, 6],
    [3, 5, 4]
]
Gasiti valoarea max si min deasupra matricilor a si b."""
# var 1
a = [
    [2, 4, 4],
    [3, 5, 6],
    [1, 5, 4]
]

b = [
    [2, 4, 4],
    [3, 9, 6],
    [3, 5, 4]
]

# Găsim maximul și minimul pentru matricea a
max_a = a[0][0]  # pornim cu primul element
min_a = a[0][0]

for linie in a:
    for elem in linie:
        if elem > max_a:
            max_a = elem
        if elem < min_a:
            min_a = elem

# Găsim maximul și minimul pentru matricea b
max_b = b[0][0]
min_b = b[0][0]

for linie in b:
    for elem in linie:
        if elem > max_b:
            max_b = elem
        if elem < min_b:
            min_b = elem

# Afișăm rezultatele
print("Matricea a: max =", max_a, ", min =", min_a)
print("Matricea b: max =", max_b, ", min =", min_b)

# var 2
a = [
    [2, 4, 4],
    [3, 5, 6],
    [1, 5, 4]
]

b = [
    [2, 4, 4],
    [3, 9, 6],
    [3, 5, 4]
]

# a) min si max din ambele matrici
valori = []
for row in a:
    valori.extend(row)

for row in b:
    valori.extend(row)

print("Min:", min(valori))
print("Max:", max(valori))

# b) matrice c (max intre elemente omologe)
c = []
for i in range(len(a)):
    linie = []
    for j in range(len(a[i])):
        linie.append(max(a[i][j], b[i][j]))
    c.append(linie)

print("c =", c)

# c) suma valorilor gasitepe liniile ambelor matrici  a si b

a = [
    [2, 4, 4],
    [3, 5, 6],
    [1, 5, 4]
]

b = [
    [2, 4, 4],
    [3, 9, 6],
    [3, 5, 4]
]

for i in range(len(a)):
    # Suma elementelor din linia i din a și linia i din b
    suma_totala = sum(a[i]) + sum(b[i])
    print(f"Linia {i+1}: suma valorilor din a și b = {suma_totala}")


