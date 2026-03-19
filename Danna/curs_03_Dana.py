"""
# Traverse a 2D object with a single for loop and integer division

integer division 2D one-for loop
no if then involved.

A =[
["a", 88, 146],
["b", 34, 124],
["c", 96, 564],
[100, 12, "d"],
]

t = ""

n = len(A) # rows
m = len(A[0]) # columns

for k in range(n * m):
    j = k % m
    i = k // m

    t += f"{k} A[{i}][{j}]={A[i][j]}\n"

print(t)
"""
from turtledemo.sorting_animate import enable_keys

"""
1. Se da vectorul a=[9,9,9,9,9,1,1,1,1,1].

a). Incrementati valorile din ultimele 6 elemente ale lui a. (Intelegera problemeni: a=[9,9,9,9,10,2,2,2,2,2] )
b). Introduceti in primele 5 elemente valorile complementare fata de 10, ale valorilor existente.
(Intelegera problemeni: a=[1,1,1,1,0,2,2,2,2,2,2] )
c) Faceti un schimb de valori intre primul si ultimul element (Swap).
(Intelegera problemeni: a = [2,1,1,1,0,2,2,2,2,1])

# 1).

a = [9,9,9,9,9,1,1,1,1,1]

n = len(a) 

for i in range(n-6, n):
    a[i] +=1

print(a)



# 2).
a=[9,9,9,9,10,2,2,2,2,2]

for i in range(5):
    a[i] = 10-a[i]

print(a)


# 3).
a=[1,1,1,1,0,2,2,2,2,2]
t=""

for i in range(5):
    t=a[0]
    a[0]=a[9]
    a[9]=t

print(a)

"""

"""
# How many 1's in matrix

a=[[1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]]

n = len(a)
m = len(a[0])
k = 0

for i in range(n):
    for j in range(m):
        if a[i][j]== 1:
            k += 1
print(k)
"""


# 2. Se da matricea binara:
# a=[[1,1,5,5,5],
#    [0,1,0,5,1],
#    [1,0,3,1,1],
#    [0,0,0,3,3],
#    [1,0,1,3,1]]
#
# Identificati valorile unice din matrice4a a si aratati frecventa fiecareia dintre ele.



"""
a=[[1,1,5,5,5],
   [0,1,0,5,1],
   [1,0,3,1,1],
   [0,0,0,3,3],
   [1,0,1,3,1]]


n= len(a)
m= len(a[0])
valori_unice = []

a = [[1, 1, 5, 5, 5],
     [0, 1, 0, 5, 1],
     [1, 0, 3, 1, 1],
     [0, 0, 0, 3, 3],
     [1, 0, 1, 3, 1]]

n = len(a)
m = len(a[0])

valori_unice = []

for i in range(n):
    for j in range(m):
        if a[i][j] not in valori_unice:
            valori_unice.append(a[i][j])

print(valori_unice)

count = []
for val in valori_unice:
    k = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == val:
                k += 1
    count.append(k)

print(count)

"""

"""
# Sum all values from matrix elements
m = [
[2, 4, 6],
[3, 5, 6],
[3, 5, 4]
]
r = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        r += m[i][j]
print(r)
"""

"""
# 7.1.3 Ex. (97) – Show matrix content
m = [
[2, 4, 6],
[3, 5, 6],

[3, 5, 4]

]

r = ""
for i in range(len(m)):
    r += "\n"
    for j in range(len(m[i])):
        r += str(m[i][j]) + " "
print(r)

"""

"""
# Show matrix content
m = [
[2, 4, 6],
[3, 5, 6],

[3, 5, 4]

]

r = ""
for i in range(len(m)):
    r += "\n"
    for j in range(len(m[i])):
        r += str(m[i][j]) + " "
print(r)
"""

"""
# 3. Se dau matricile:

m=[
   [2,4,6],
   [3,5,6],
   [3,5,4] 
]

t=[
    [1,1,1],
    [3,5,6],
    [3,5,4]
]

a) Faceti suma intre elementele omolog si stocati rezultatul intr-o matrice c.


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

r= ""
c = []

for i in range(len(m)):
    linie = []
    for j in range(len(m[i])):
        linie.append(m[i][j] + t[i][j])
    c.append(linie)

    r += str(linie) + "\n"  # inseamna linie noua

print(r)
"""

"""
# Multiplication involving a scalar and a matrix.

m = [
[2, 4, 6],
[3, 5, 6],
[3, 5, 4]
]
s = 3  # scalar
for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j] = s * m[i][j]
        # m[i][j] *= s
print(m)
"""

"""
b). Se da o matrice binara:
q=[
    [1,1,1],
    [0,0,0],
    [0,0,1]
    ]
Folositi matricea q ca harta pentru operatii. Anume, valoarea 1 din q trebuie sa duca la 
insumarea valorilor din elementele omolog ale lui m si t, iar valoarea 0 din q trebuie sa duca la
inmultire cu un scalar s=3, ale elementului omolog din t.
"""

"""
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
r = ""

for i in range(len(m)):
    for j in range(len(m[i])):
        if q[i][j] == 1:
            val = m[i][j] + t[i][j]
        else:
            val = t[i][j] * s

        r += str(val) + " "
    r += "\n"

print(r)

"""

"""
# Sum all values from the rows of the matrix
m = [
[2, 4, 4],
[3, 5, 6],
[3, 5, 4]
]
r = []
for i in range(len(m)):
    # Initialize r[i] to 0.
    r.append(0)
    for j in range(len(m[i])):
        r[i] += m[i][j]
print(r)
"""

"""
# Sum all values from the colums of the matrix
m = [
[2, 4, 4],
[3, 5, 6],
[3, 5, 4]
]
c = []
for i in range(len(m)):
    for j in range(len(m[i])):
        if len(c) <= j:
            c.append(0)
        c[j] += m[i][j]
        # c[j] *= m[i][j]
print(c)
"""
"""
4. Se dau matricile a si b:
a = [
    [2, 4, 4],
    [3, 5, 6],
    [1, 5, 4]
]

b=[
    [2, 4, 4],
    [3, 9, 6],
    [3, 5, 4]
]

a). Gasiti valoarea minima si maxima deasupra matricilor a si b
b). Formulati o matrice c care sa contina valoarea cea mai mare gasita intre elementele emolog ale lui a si b
c). faceti suma valorilor gasite pe liniile ambelor matrici a si b.
"""


"""
a).
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

min_a = min(min(row) for row in a)
max_a = max(max(row) for row in a)

min_b = min(min(row) for row in b)
max_b = max(max(row) for row in b)

print("min:", min(min_a, max_a, min_b, max_b))
print("max:", max(min_a, max_a, min_b, max_b))

"""

"""
b).
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

r = []
c= ""

for i in range(len(a)):
    linie = []
    for j in range(len(a[i])):
        if a[i][j] > b[i][j]:
            linie.append(a[i][j])
        else:
            linie.append(b[i][j])
    r.append(linie)
    c += str(linie) + "\n"


print("Matricea c:", c)
"""


"""
c).
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

n=[]

for i in range(len(a)):
    # Initialize n[i] to 0.
    n.append(0)
    for j in range(len(a[i])):
        n[i] += a[i][j]
#print(n)

r = []
for i in range(len(b)):
    # Initialize r[i] to 0.
    r.append(0)
    for j in range(len(b[i])):
        r[i] += b[i][j]
#print(r)

m=[]
for i in range(len(n)):
    m.append(n[i] + r[i])

print(m)


# sau altfel scris c).
# for i in range(len(a)):
#     # Suma elementelor din linia i din a și linia i din b
#     suma_totala = sum(a[i]) + sum(b[i])
#     print(f"Linia {i+1}: suma valorilor din a și b = {suma_totala}")

"""


"""
# Matrix multiplication with three for loops
a = [
[2, 4, 6],
[3, 5, 6],
[3, 5, 4]

]

b = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
]
c = []
r = ""
for i in range(len(a)):
    r += "\n"
    c.append([])
    for j in range(len(a[i])):
        c[i].append(0)
        for k in range(len(a[i])):
            c[i][j] += a[k][j] * b[i][k]
        r += str(c[i][j]) + " "
print(r)

"""

"""
# Matrix multiplication with two for loops 
a = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
    ] 
b = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
    ] 
i = j = 0 
r = "" 
c = [] 
n1 = len(a) 
n2 = len(a[0]) 
q = n1 * n2 
c.append([]) 
for v in range(q):
    j = v % n2
    if j==0 and v!=0 and i<n1 and v!=q:
        i += 1
        
    c.append([])
    r += "\n"
    c[i].append(0)
    for k in range(len(a[i])):
        c[i][j] += a[k][j] * b[i][k]
        r += str(c[i][j]) + " "
 
Output: 
34 58 60 
39 67 72 
33 57 64
 
print(r)
"""

"""
# Multiply specific elements of two matrices based on a map
a = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
    ] 
b = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
    ] 
c = [
    [2, 4, 6],
    [3, 5, 6],
    [3, 5, 4]
    ] 
n = len(a) 
m = len(a[0]) 
r = '' 
for i in range(n):
    r += '\n'
    for j in range(m):
        if b[i][j] == 1:
 
            c[i][j] = a[i][j] * c[i][j]
        r += str(c[i][j]) + " " 
print(r)
"""

"""
# Different operations based on maps 
# perform different operations between 
# the values of the homologous elements 
# of two arrays based on a map/model 
# (third array). 
a = [
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2]
    ] 
b = [
    [1, 1, 0, 0, 0],
    [3, 1, 0, 0, 1],
    [1, 3, 0, 1, 1],
    [0, 0, 0, 7, 0],
    [3, 0, 4, 0, 9]
    ] 
c = [
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 1]
     ] 
n = len(a) 
m = len(a[0]) 
r = '' 
for i in range(n):
    r += '\n'
    for j in range(m):
        if b[i][j] == 0:
            c[i][j] = a[i][j] * c[i][j]
        if b[i][j] == 1:
            c[i][j] = a[i][j] + c[i][j]
        if b[i][j] == 2:
            c[i][j] = a[i][j] - c[i][j]
        if b[i][j] == 3:
            c[i][j] = c[i][j] - a[i][j]
        if b[i][j] == 4:
            c[i][j] = a[i][j] % c[i][j]
        if b[i][j] == 5:
            c[i][j] = a[i][j] / c[i][j]
        if b[i][j] == 6:
            c[i][j] = a[i][j]
        if b[i][j] == 7:
            c[i][j] = '#'
        if b[i][j] == 8:
            pass  # Placeholder for "do stuff"
        if b[i][j] == 9:
            if c[i][j] <= a[i][j]:
                c[i][j] = a[i][j]
        r += str(c[i][j]) + " " 
print(r)
"""

"""
# Built-in sin, exp

import math

a = 3.1415
b = math.sin(a)

c = math.exp(math.sin(a))
print(b)
print(c)

"""

"""
# Cascading built-in functions (split, join, length)
a = "----##----------##--------"

q = "##"
b = len(a)
c = len(a.replace(q, ""))
if c < b:
    print("a contains q")
    print((b - c)/len(q)) # de cate ori a contine q
"""

