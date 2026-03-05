"""
print ('Hello World')


# exemplu1
A=1
a=2
a1=3
a_1=4

print(A)
print(a)
print(a1)
print(a_1)


# exemplu2
a=3
b=5
c=a+b
print(c)


# exemplu3
a=3
b=a
print(a)

# exemplu4
a='text'
b='text'
b=0


# exemplu5

a=3
b=2 
c=a+b/2-a*b
print(c)

# exemplu6
a=2
a=a+1  # sau a+=1
print(a)

# exemplu7
a=2
a=a+a
print(a)


# exemplu7
a=2
a=a-a
a=a-1
print(a)


# exemplu8
a=2
a+= a-1
a+= a-1
print(a)

# exemplu9
a=3
b=7
t=0

t=a
a=b
b=t

print('a=',a)
print('b=',b)

# exemplu10
a=3
b=a+7
a=None
# c=a+b  voi avea o eroare pt ca nu pot aduna NoneType + int
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
print(a)
print(b)

# exemplu11
s = (1+2+3+4+5+6+7+8)
print(s)

# exemplu12 - formatare output

a=3
b=7
c=10
r= "a = " + str(a) + " and b= " + str(b)
t= " is a number.\n"
l = str(a+b/c) + t
print(l+r)


#exemplu13

a=4
b=7
if a<b:
  print(a)
else:
    print(b)

# exemplu14

a=2
b=3
c=1

if a<b:
    c=0

print(c)

# exemplu15

a=1
b=2
c=3
if a<b:
    c += 1
else:
    c -= 1

print("c=" + str(c))


# exemplu16

a=1
b=2
c=3
if a<b:
    c -= 1
elif b ==c:
    c += 1
else:
    c = 0
print("c=" + str(c))

# exemplu17

a=1
b=0
if a==0:
    b=11
elif a==1:
    b=64
elif a==2:
    B=33

print(b)


# LOOPS

# ex1
i = 0
while i <5:
    print("i= ", i)
    i+=1

# ex2
i = 0

while True:
    print("i ="+ str(i))
    i += 1
    if i >= 5:
        break

# ex3
for i in range(5):
    print(5 - i)

# ex4 -  mergi pornind de la 10, 5 elemente, descrescator cate 1, -1 este range, [10,5) este perioada
for i in range(10, 5, -1):
    print(i)

# ex5

i = 10
while i > 5:
    i -= 1
    print(i)
    i -= 1

# ex6
a = 5

for i in range(a):
    print(a - i)

# ex7
a = 0

for i in range(1, 6):
    a = a + (i + 4 * 3)

print(a)


# ex8
a = 0

for i in range(11):
    a = a + i

print(a)

# ex9 - sum all results od addition of 1 in a nxn cycle

r = 0
for i in range(10):
    for j in range(10):
        r += 1

print(r)

# ex10
r = 0
for i in range(4):
    for j in range(4):
        r += 3

print(r)

# ex11
r = 0
for i in range(10):
    for j in range(10):
        r += j * i

print(r)

# ex12
a = 0
m = 3
n = 5

for j in range(1, m + 1):
    for i in range(1, n + 1):
        a = a + (i + j * 3)

print(a)

# ex13
a = 0

# In Python, range
# end is exclusive.

for j in range(1, 4):
    for i in range(1, 6):
        a = a + (i + 1 * 3)

print(a)

# ex14
a = 0
m = 3
n = 5

for j in range(1, m + 1):
    for i in range(1, n + 1):
        a = a + (i + j * m)

print(a)

# ex15
a = 0
m = 4

for j in range(1, m+1):
    for i in range(1, j+1):
        a = a + (i + j * m)

print(a)

# ex16
a=0
m=5
n=7

for j in range(1, m + 1):
    for i in range(j, n + 1):
        a += (i + j * m)

print(a)

# ex17
for i in range(2):
    for j in range(3):
        print(f"i = {i}, j = {j}")

# ex18
i = j = 0
n1 = 2
n2 = 3
q = n1 * n2

for v in range(q):
    j = v % n2
    if j == 0 and v != 0 and i < n1 and v != q:  # ! inseamna negatie
        i += 1
    print(f"i = {i}, j = {j}")

# ex19

#a[i] vector
# a[i][j] = matrix
# a[i][j][x] = tensor
# a[i][j][x][y] ...

a = [2, 5, 7]
b = [6, 8]

print(a + b)  # se face concatenarea celor 2 vectori

# ex20

a = [2, 5, 7]
b = [6, 8]
c = a[1] + b[0]
print(c)

# ex21 - adding elements

A = []

A.append("a")
A.append("b")
A.append("c")

print(A[0]+ A[1] +A[2])

# ex22 - using array literals of different data types
A = []
B = []

A = ["a", "b", "c"]
B = [1, 2, 3]

print(A[0]+A[1] +A[2])  # concateneaza valorile
print(B[0]+ B[1] + B[2]) # aduna valorile


# ex23
A = ["a", "b", "c"]

x = A[1]
y = A[2]

print(x + y)

# ex24
A = ["a", "b", "c"]

x= A[1]

A[0] = "d"
A[1]= A[2]
A[2] = x

print(A[0]+A[1] + A[2])


# ex25
a = [2, 5, 7]
b = [6, 8]

a[1] -= 1
b[0] -= 1

c= a[1] + b[0]

print(c)


# ex26

a=[5,6,8]
b= len(a)
print(b)


# ex27
A = [1, 2, 3]

if A[0] < A[1]:
    A[2] += 1

print("A[2]="+ str(A[2]))
"""

# ex28
A = ["a", "b", "c", "d", "e", "f", "g"]

i = 0
t = ''

while i < len(A):
    t += "\n i[" + str(i) + "]=" + A[i]
    i += 1

print(t)