# ------------------------ Ex92: Traverse a 2D object with a single for loop and integer division
"""
A = [
    ["a", 88, 146],
    ["b", 34, 124],
    ["c", 96, 564],
    [100, 12, "d"],
]

t = ""
n = len(A)   # rows
m = len(A[0]) # columns

for k in range(n * m):
    i = k // m  # row -> DIVIZIUNEA NUMERELOR INTREGI
    j = k % m   # column
    t += f"{k} A[{i}][{j}]={A[i][j]}\n"

print(t)
"""

# -------------------------------Ex sumplimentar

# Se da vectorul a= [9,9,9,9,9,1,1,1,1].
# 1. Incrementati valorile din ultimile 6 elemente ale lui a.
# 2. Introduceti in primele 5 elemente valorile complementare fata de 10, ale valorilor existente.

# Rezolvare cerinta 1:
"""
a = [9,9,9,9,9,1,1,1,1,1]

for i in range(len(a) - 6, len(a)):
    a[i] += 1

print(a)
# Intelegerea problemei:
"""

"""

# Rezolvare cerinta 2:

a = [9, 9, 9, 9, 10, 2, 2, 2, 2, 2]

for i in range(5):
    a[i] = 10 - a[i]

print(a)
"""
# Cerinta 3. Faceti un schimb de valori intre primul si ultimul element(Swap):
"""
a = [1, 1, 1, 1, 0, 2, 2, 2, 2, 2]

a[0], a[-1] = a[-1], a[0]

print(a)
"""
# Cerinta 4: Identificati valorile unice din matrice si aratati frecventa fiecaruia dintre ele.
"""
a = [[1, 1, 5, 5, 5],
    [0, 1, 0, 5, 1],
     [1, 0, 3, 1, 1],
     [0, 0, 0, 3, 3],
     [1, 0, 1, 3, 1]]
"""
"""
# REZOLVARE:
a = [[1, 1, 5, 5, 5],
     [0, 1, 0, 5, 1],
     [1, 0, 3, 1, 1],
     [0, 0, 0, 3, 3],
     [1, 0, 1, 3, 1]]

frecventa = {}

for row in a:
    for val in row:
        if val in frecventa:
            frecventa[val] += 1
        else:
            frecventa[val] = 1

print(frecventa)
"""

# 7.1.2 Ex. (96) – Sum all values from matrix elements
""" 
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
# Cerinta 5:
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

r = ""
c = []

for i in range(len(m)):
    linie = []
    for j in range(len(m[i])):
        linie.append(m[i][j] + t[i][j])
    c.append(linie)

    r += str(linie) + "\n"

print(r)
"""
# 7.1.4 Ex. (98) – Multiplication involving a scalar and a matrix.
"""
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
# Cerinta 6:
"""Se da matricea binara:
q=[
[1,1,1],
[0,0,0],
[0,0,1]
]
Folositi matricea q ca harta pt operatii. 
Anume, valoarea 1 din q trebuie sa duca la sumarea valorilor din elementele omolog ale lui m si t,
iar valoarea 0 din q trebuie sa duca la o inmultire cu un scalar s = 3, ale elementului omolog din t"""
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
# Ex: Se dau matricile a si b:
"""
a = [
[2, 4, 4],
[3, 5, 6],
[1, 5, 4]
]

b = [
[2, 4, 4],
[3, 9, 6],
[3, 5, 4]

a) Gasiti valoarea minima si maxima deasupra matricilor a si b.
b) Formulati o matrice c, care sa contina valoarea cea mai mare gasita intre elementele omolog
ale lui a si bJ
c) Faceti suma valorilor gasite pe liniile ambelor matrici a si b.
"""
"""
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
    # Initialize r[i] to 0.
    n.append(0)
    for j in range(len(a[i])):
        n[i] += a[i][j]
print(n)

r = []
for i in range(len(b)):
    # Initialize r[i] to 0.
    r.append(0)
    for j in range(len(b[i])):
        r[i] += b[i][j]
print(r)
"""
# -------------- Ex 102:
"""
# 7.1.8 Ex. (102) – Multiply all values from the columns / rows and store them in array
m = [
[2, 4, 4],
[3, 5, 6],
[3, 5, 4]

]
# Initialize a with
# default values.
a = [[1 for _ in range(len(m[0]))], \
     [1 for _ in range(len(m))]]
for i in range(len(m)):
    for j in range(len(m[i])):
        # Check if the element
        # exists, if not
        # initialize to 1.
        # In Python, this check
        # is not necessary since
        # we have initialized all
        # elements to 1.
        # if not a[0][j]: a[0][j] = 1
        # if not a[1][i]: a[1][i] = 1
        a[0][j] *= m[i][j]
        a[1][i] *= m[i][j]
        # The commented out code
        # is an alternative
        # calculation, not used in
        # the active code.
        # if not a[0][j]: a[0][j] = 0
        # if not a[1][i]: a[1][i] = 0
        # a[0][j] += m[i][j]
        # a[1][i] += m[i][j]
print('C =', a[0])
print('R =', a[1])
# or another version:
m = [
    [2, 4, 4],
    [3, 5, 6],
    [3, 5, 4]
]
a = [[1] * len(m[0]), [1] * len(m)]
for i in range(len(m)):
    for j in range(len(m[i])):
        a[0][j] *= m[i][j]
        a[1][i] *= m[i][j]
print('C = ' + str(a[0]))
print('R = ' + str(a[1]))
"""
# 7.1.9 Ex. (103) – Sum all values from the right diagonal of the square matrix
"""
a = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]

]
d = 0
n = len(a)
m = len(a[0])
i = 0
while i < n:
    j = 0
    while j < m:
        d += a[i][m - j - 1]
        print(a[i][m - j - 1])
        i += 1
        j += 1
print('---\n' + str(d))
# or a second version:
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
d = 0
n = len(a)
m = len(a[0])
i = 0
for j in range(m):
    d += a[i][m - j - 1]
    print(a[i][m - j - 1])
    i += 1
print('---\n' + str(d))
"""
# 7.1.10 Ex. (104) – Sum all values from the left diagonal of the square matrix
"""
a = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
d = 0
n = len(a)
m = len(a[0])
i = 0
for j in range(m):
    d += a[i][j]
    print(a[i][j])
    i += 1
print('---\n' + str(d))
"""
# 7.1.11 Ex. (105) – Sum all values from the left and right diagonal of a square matrix
"""
a = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2],
[3, 4, 5, 6]
]
ld = 0
rd = 0
n = len(a)
m = len(a[0])
i = 0
for j in range(m):
    ld += a[i][j]
    rd += a[i][m - j - 1]
    i += 1
print('L=' + str(ld) + '|R=' + str(rd))
"""
# 7.1.13 Ex. (107) – Show bottom – left part of the matrix
"""
a = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2],

[3, 4, 5, 6]

]

d = []
n = len(a)
r = ''
for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[i][j])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)

"""
# 7.1.14 Ex. (108) – Show bottom – left part of the matrix and flip horizontal
"""
a = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2],

[3, 4, 5, 6]

]

d = []
n = len(a)
m = len(a[0])
r = ''
for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[i][i - j])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2],
    [3, 4, 5, 6]
]

n = len(a)
m = len(a[0])
r = ''

d = []  # lista pentru partea dreaptă
for i in range(n):
    # adaugăm un rând cu valori None
    d.append([None] * m)
    for j in range(i, m):
        d[i][j] = a[i][j]
        r += str(d[i][j]) + ' '
    r += '\n'

print(r)
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 0, 1, 2], 
    [3, 4, 5, 6]
]

n = len(a)
r = ''
d = []

for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[i - j][i])
        r += str(d[i][j]) + ' '
    r += '\n'

print(r)
# 7.1.17 Ex. (111) – Show top – right, flip 90 degrees left and flip horizontally
a = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2],
[3, 4, 5, 6]
]



d = []
n = len(a)
r = ''
for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[j][i])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)

# 7.1.18 Ex. (112) – Secondary diagonal scan (right)
a = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2],

[3, 4, 5, 6]

]

d = []
n = len(a)
r = ''
for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[j][i - j])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2], 
    [3, 4, 5, 6]                  
]

n = len(a)
m = len(a[0])
d = []
r = ''

for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[i - j][n - 1 - j])
        r += str(d[i][j]) + ' '
    r += '\n'

print(r)
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 0, 1, 2], 
    [3, 4, 5, 6]
]

n = len(a)
m = len(a[0])
r = ''
d = []

for i in range(n):
    d.append([])
    for j in range(i + 1):
        d[i].append(a[i][m - j - 1])
        r += str(d[i][j]) + ' '
    r += '\n'

print(r)
# 7.1.21 Ex. (115) – Matrix flip vertical
# flip vertical.                 Output:
a = [
[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 0, 1, 2],
     [3, 4, 5, 6]
     ]
d = []
n = len(a)
m = len(a[0])
r = ''
for i in range(n):
    # Initialize the
    # inner list.
    d.append([0] * m)
    for j in range(m):
        d[i][j] = a[n - i - 1][j]
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)
# 7.1.22 Ex. (116) – Matrix flip horizontal
# flip horisontal.               Output:
a = [
[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 0, 1, 2],
     [3, 4, 5, 6]
     ]
d = []
n = len(a)
m = len(a[0])
r = ''
for i in range(n):
    d.append([])
    for j in range(m):
        d[i].append(a[i][m - j - 1])
        r += str(d[i][j]) + ' '
    r += '\n'
print(r)
# 7.1.23 Ex. (117) – Sum values from elements of a matrix based on a map
a = [
[2, 4, 6],
[3, 5, 6],
[3, 5, 4]
]
b = [
    [0, 0, 1],
    [1, 1, 0],
    [0, 0, 1]
]
n = len(a)
m = len(a[0])
r = 0
for i in range(n):
    for j in range(m):
        if b[i][j] == 1:
            r += a[i][j]
print(r)
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

# Variante cu pre-alocare
c = [[0] * len(a[0]) for _ in range(len(a))]
r = ""

for i in range(len(a)):
    r += "\n"
    for j in range(len(a[i])):
        c[i][j] = a[i][j] + b[i][j]
        r += str(c[i][j]) + " "

print(r)
"""
# 7.1.25 Ex. (119) – Matrix multiplication with three for loops
"""
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

# 7.1.26 Ex. (120) – Matrix multiplication with two for loops
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
    if j == 0 and v != 0 and i < n1 and v != q:
        i += 1
    c.append([])
    r += "\n"
    c[i].append(0)
    for k in range(len(a[i])):
        c[i][j] += a[k][j] * b[i][k]
        r += str(c[i][j]) + " "
print(r)
# 7.1.27 Ex. (121) – Multiply specific elements of two matrices based on a map
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
# 7.1.28 Ex. (122) – Different operations based on maps
# perform different operations between Output:
# the values of the homologous elements
# of two arrays based on a map/model 5 5 6 6 6
# (third array).                   1 5 6 6 5
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

def SMC(m):
    r = "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += " " + str(m[i][j]) + " "
        r += "\n"
    return r

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
m_len = len(a[0])

for i in range(n):
    for j in range(m_len):
        if b[i][j] == 0:
            c[i][j] = a[i][j] * c[i][j]
        elif b[i][j] == 1:
            c[i][j] = a[i][j] + c[i][j]
        elif b[i][j] == 2:
            c[i][j] = a[i][j] - c[i][j]
        elif b[i][j] == 3:
            c[i][j] = c[i][j] - a[i][j]
        elif b[i][j] == 4:
            c[i][j] = a[i][j] % c[i][j]
        elif b[i][j] == 5:
            c[i][j] = a[i][j] / c[i][j]
        elif b[i][j] == 6:
            c[i][j] = a[i][j]
        elif b[i][j] == 7:
            c[i][j] = ' #'
        elif b[i][j] == 8:
            pass  # Placeholder
        elif b[i][j] == 9:
            if c[i][j] <= a[i][j]:
                c[i][j] = a[i][j]

print(SMC(c))

# 7.1.30 Ex. (124) – Nested arrays
A = ["a", "b", "c"]

B = ["d", "e", "f"]
C = ["g", "h", "i"]

D = [A, B, C]

E = [B, C, A]
F = [C, B, A]
G = [D, E, F]
print(A[0])
print(D[0])
print(G[0])

"""

# 8.1.1 Ex. (125) – Built-in sin, exp
"""
import math

a = 3.1415

b = math.sin(a)

c = math.exp(math.sin(a))
print(b)
print(c)

# 8.1.6 Ex. (130) – Random integers from 0 to 99 in an array
import random

a = []

n = 10

for k in range(n):
    a.append(random.randint(0, 99))
print(a)

# 8.1.7 Ex. (131) – Insert random values in the elements of a matrix.
import random

p = []

n = 3

m = 3

r = ''

for i in range(n + 1):
    p.append([])
    for j in range(m + 1):
        p[i].append(random.randint(0, 9))
        r += str(p[i][j]) + ' '
    r += '\n'
print(r)

# 8.1.8 Ex. (132) – Split string to integers by using a delimiter symbol
b = []

a = '2#5#7#1#1#2'
b = a.split('#')

print("b = " + str(b))
# 8.1.9 Ex. (133) – Split string to array by using the “|” symbol
n = []

m = []
c = 'AAAAA|BBBBB|CCCCC'
n = c.split('|')
print(n[2])
"""
# 8.1.10 Ex. (134) – Cascading built-in functions (split, join, length)
"""
a = "----##----------##--------"
q = "##"
b = len(a)
c = len(a.replace(q, ""))

if c < b:
    print("a contains q")

# numărul de apariții
occurrences = (b - c) // len(q)
print(occurrences)
"""
# 8.1.11 Ex. (135) – Built-in sort function
b = [3, 6, 2, 78, 99, 1, 4]
b.sort() # lipseste de aici
print(b)

def compute(x):
    return x + x / x - x * x

# apelul funcției în afara definiției
a = 10
b = compute(a)
print(b)

# 8.2.2 Ex. (137) – Making of a function with more than one parameter
def mul(a, b):
    return a * b
print(mul(2, 5))

# 8.2.3 Ex. (138) – Gauss summation - sum all from 0 to n
def gs(n):
    return n * (n + 1) // 2
print(gs(100))

# 8.2.4 Ex. (139) – Function calls to other functions
def daniela(a, b):
    return a + b

def sebastian(a, b):
    p = daniela(a, b)
    return p


def main_app(x, y):
    cc = sebastian(x, y)
    return cc


d = main_app(66, 100)
print(d)

# --------------- Ex 140
def compute(x):
    return x + x / x - x * x

def distribution(start, stop):
    t = ""
    for i in range(start, stop):
        t += str(compute(i)) + "\n"
    return t

a = distribution(3, 21)
print(a)

# 8.2.6 Ex. (141) – Function chaining - nested function calls
def c(x):
    return x + x / x - x * x
a = 3
b = c(c(c(c(a))))
b = -b
print(b)

# 8.2.7 Ex. (142) – Function composition
a = [1, 2, 3, 4, 5]

t = 0


def c1(t, a):
    return 5 + c2(t, a)


def c2(t, a):
    return c3(t, a) + 5


def c3(t, a):
    s = 1
    return s + c4(t, a)


def c4(t, a):
    return c5(t, a) + c5(t, a)


def c5(t, a):
    for i in a:
        t += i
    return t


b = c1(t, a)
print(b)
# ------------- Ex 143
a = 3.1415  # constant
b = 11      # global variable

def compute():
    x = b
    return x + x / x - x * x

b = compute()

print(f"{b}\n{a}")

 # ---------- Ex144:
def pure(x):
    return x + x / x - x * x

def inpure(x):
    global a
    a = 11
    return x + x / x - x * x

a = 10
b = pure(a)
print(str(b) + " & " + str(a))

c = inpure(a)
print(str(c) + " & " + str(a))

d = inpure(a)
print(str(d) + " & " + str(a))

# ----------- Ex 145
a = 16

def f(x):
    return x + x / x - x * x

def p():
    global b
    x = a - 11
    b = x + x / x - x * x
    b = f(a)
    print(b)

p()
print(b)

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

