#------------------------Ex2. Naming variables

A = 1
a = 2
a1 = 3
a_1 = 4

print("A: ",A)
print("a: ",a)
print("a1: ",a1)
print("a_1: ", a_1)

#-----------------------Ex3: Write your first Python program:

a=3
b=5
c=a+b
print("c: ",c)

#-------------------------Ex4: The meaning of "a=b":
a = 3
b = a
print("b",b)

#------------------------Ex5: Assign and reasign witg type change:

# In Python, one simply assigns a
# value to a variable to declare it.

# Assigns a string 'text'
# to variable a.
a = 'text';

# a = 0; # For sport, one can
# uncomment this line (a = 0;)
a=0;
# to reassign a to a numeric value.

# Assigns a string 'text
# to variable b.
b = 'text';
b=0; #Reassigns b to a numeric value

#----------------------------Ex6: Basic mathematical operations:
a=3
b=2
c=a+b/2-a*b;
print("c: ",c)

#---------------------------Ex7: The meaning of modulo operator:
a=3
a=a%2;
print("a: ",a)

#---------------------------Ex8: The meaning of "a=a+1":
a=2
a=a+1 #incrementare varianta 1
print("a: ",a)

#---------------------------Ex9: The aggregate asignment:
a=2
a +=1 #incrementare varianta 2
print("a: ",a)

#-------------------------Ex10: The plus operator:
a=2;
a=a+a;
print("a: ",a)

#-------------------------Ex11: The minis operator
a=2;
a=a-a;
a=a-1;
print("a: ",a)

#------------------------Ex12: Variable playground:
a = 2
a += a - 1
a += a - 1
print("a",a)

#------------------------Ex.13 - Swap values

a = 3
b = 7
t = 0

t = a
a = b
b = t

print ('a =', a)
print('b =', b)

#-------------------------Ex14: Empty a variable

a = 3
b = a + 7
a = None
# c=a+b
print("a: ",a)
print("b: ",b)
# print(c) -----#da eroare: TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

#------------------------Ex15:Line continuation:
s= (1+ 2 + 3 +
4 + 5 + 6 + 7 + 8)
print("s: ",s)

#-----------------------Ex16: Formated output:
a = 3
b = 7
c = 10
r = "a = " + str(a) + " and b = " + str(b)
t = " is a number. \n"
l = str((a + b /c)) +t
print("l+r: ",l + r)

#----------------------Ex17: If then else - conditional statements (I):

a = 4
b = 7
if a < b:
    print("printeaza a:",a)
else:
    print("printeaza b",b)

#---------------------Ex18: If then else - conditional statements (II):
a = 2
b = 3
c = 1

if a < b:
      c = 0
print(c)

#---------------------Ex19: If then else - conditional statements (III):
a = 1
b = 2
c = 3

if a < b:
    c += 1
else:
    c -= 1

print("c=" + str(c))

#---------------------Ex20: If then elseif else - conditional statements
a=1
b=2
c=3

if a < b:
    c -= 1
elif b == c:
    c += 1
else:
    c = 0
print("c=" + str(c))

#---------------------Ex21: Alt exercitiu:
a = 1
b = 0

if a == 0:
    b = 11
elif a == 1:
    b = 64
elif a == 2:
    b = 33
print(b)

#--------------------Ex22: While Loop   :
i = 0

while i < 5:
    print("i =", i)
    i += 1

#-------------------Ex23: Do while:
i = 0

while True:
    print("i ="+ str(i))
    i += 1
    if i >= 5:
        break

#-------------------Ex24: Revers by substraction from the upper limit:
for i in range(5):
    print(5-i)

#------------------Ex25: Reverse for-loop:
for i in range(10, 5, -1):
    print(i)

#-------------------Ex26: The meaning of before and after:
i = 10
while i > 5:
    i -= 1
    print("print i: ",i)
    i -= 1

#-------------------Ex27:  Revers by substraction from the upper limit variable:

a = 5

for i in range(a):
    print(a - i)

#-------------------Ex28: For lopp sumation:
a = 0

for i in range(1, 6):
    a = a + (i + 4 * 3)
print(a)

#-------------------Ex29: Simple counter sumation:
a = 0

for i in range(11):
    a = a + i

print(a)

#--------------------Ex30: Sum all results of addition of 1 in a nxn cycle
r = 0
for i in range(10):
    for j in range(10):
        r += 1

print(r)

#---------------------Ex31: Sum all results of addition of 3 in a nxn cycle:

r = 0
for i in range(4):
    for j in range(4):
        r += 3

print(r)

#-------------------Ex32: Sum all results of the multiplication betweeen i and j:
r = 1
for i in range(10):
    for j in range(10):
        r += j * i

print(r) # anul 2026

#------------------Ex33: Nested for loo[s and summation of counter variables:
a = 0
m = 3
n = 5

for j in range(1, m + 1):
    for i in range(1, n + 1):
        a = a + (i + j * 3)

print(a)

#--------------------Ex34:  Nested for loops and summation based on the inner counter

a = 0
# In Python, range
# end is exclusive.

for j in range(1, 4):
    for i in range(1, 6):
        a = a + (i + 1 * 3)
print(a)

#-----------------------Ex35: Nested for loops & summation based on counters and upper limits (I)

a = 0
m = 3
n = 5

for j in range(1, m +1):
    for i in range(1, n + 1):
        a = a + (i + j * m)
print(a)

#----------------------Ex36:  Nested for loops & summation based on counters and upper limits (II)

a = 0
m = 4

for j in range(1, m+1):
    for i in range(1, j+1):
        a = a + (i + j * m)
print(a)

#-----------------------Ex37:Nested for loops & summation based on counters and upper limits (III)
a = 0
m = 5
n = 7
for j in range(1, m + 1):
    for i in range(j, n + 1):
        a += (i + j * m)

print(a)

#----------------------Ex38: Show i and j coordinates at each step:

for i in range(2):
    for j in range (3):
        print(f"i = {i}, j = {j}") # f-> format (formateaza); {i} -> i ca valoarea lui i

#----------------------Ex39: One for loop that simulates two for loops:
i = j = 0
n1 = 2
n2 = 3
q = n1 * n2

for v in range(q):
    j = v % n2
    if j == 0 and v != 0 and i < n1 and v != q:
        i += 1
    print(f"i = {i}, j = {j}")

 # LISTS
#---------------------Ex40:Array addition

# a[i] vector
# a[i][j] = matrix
# a[i][j][x] = tensor
# a[i][j][x][y] ...

a = [2, 5, 7]
b = [6, 8]

print(a + b)

#-----------------------Ex41: Extracting individual values from the elements of an array:

a = [2, 5, 7]
b = [6, 8]
c = a[1] + b[0]
print(c)

#-----------------------Ex42: Adding elements:
A = []

A.append("a") #metoda append care adauga in lista []
A.append("b")
A.append("c")

print(A[0]+A[1] + A[2]) #le leaga pt ca e concatenare
# output: abc

#---------------------Ex43: Using array literals of different data type:
A = []
B = []

A = ["a", "b", "c"]
B = [1, 2, 3]

print(A[0]  +A[1] + A[2]) #output: abc
print(B[0] + B[1] + B[2]) #output: 6

#---------------------Ex44: Accessing array elements:
A = ["a", "b", "c"]

x = A[1]
y = A[2]

print(x + y) #output: bc

#--------------------Ex45:Changing values in array elements - swap values or replace

A = ["a", "b", "c"]

x = A[1]

A[0] = "d"
A[1]= A[2]
A[2] = x

print(A[0]+A[1]+A[2]) #Output :dcb

#------------------Ex46:  Extracting individual values from the elements of an array

a = [2, 5, 7]
b = [6, 8]

a[1] -=1
b[0] -=1

c = a[1] + b[0]

print(c) #output: 9

#-----------------Ex47: Array length:
a = [5,6,8]
b = len(a)
print(b) #output: 3

#----------------Ex48:  Accessing the values from the components of an array

A = [1, 2, 3]

if A[0] < A[1]:
    A[2] += 1

print("A[2]="+ str(A[2])) #output: A[2]=4

#-----------------Ex49: Traverse a 1D array using a while loop (I)

A = ["a", "b", "c", "d", "e", "f", "g"]

i = 0
t = ''

while i < len(A):
    t += "\n i[" + str(i) + "]=" + A[i]
    i += 1

print(t)
