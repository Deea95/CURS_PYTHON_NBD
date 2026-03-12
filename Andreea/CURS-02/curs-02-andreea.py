# Curs 2 - 12.03.2026

# Operatori Python:
"""
a = 2
b = 3
print("a+b=", a+b)
print("a-b=", a-b)
print("a*b=", a*b)
print("a/b=", a/b)
print("a//b=", a//b)
print("a%b=", a%b)
print("a**b=", a**b)
print("a/b=", a/b)
print("a//b=", a//b)
print("a%b=", a%b)
print("a**b=", a**b)
print("a/b=", a/b)
print("a//b=", a//b)
"""

#-----------------Ex50: Traverse a 1D array using a while loop (II)
"""
A = ["a", "b", "c", "d", "e", "f", "g"]
i = 0
t = ''
while i < len(A):
    t += "\n i[" + str(i) + "]=" + A[len(A)-i-1]
    i += 2
print(t)
"""
#-----------------Ex51: Traverse a 1D array using a for loop
"""
A = ["a", "b", "c", "d", "e"]

t = ""

for i in range(len(A)):
    t += "\n A[" + str(i) + "]=" + A[i]

print(t)
"""
#-----------------Ex52: The for a in b
"""
a = ["x", "y", 2]

for b in range(len(a)):
    print(a[b])
"""
#-----------------Ex53: Print all integers from array using a for loop
"""
a = [5, 6, 8]

for j in range(len(a)):
    print(a[j])
"""
#-----------------Ex54: Sum all values from array
"""
a = [5, 6, 8]
b = 0

for j in range(len(a)):
    b = b + a[j]
print(b)
"""
#-----------------Ex55: Multiplication involving a scalar and a 1D array
"""
a = [5, 6, 8]

for j in range(len(a)):
    a[j] = 2 * a[j]

print(a)
"""
#-----------------Ex56: Insert values into an array
"""
a = []

# In Python, the range end
# is exclusive, so we use
# 11 to include 10.

for j in range(11):
    a. append (j)

print(a)
"""
#-----------------Ex57: Insert ascending and descending integer values into arrays
"""
a = []
b = []

# range(11) to include 10,
# since range in Python is
# upper-bound exclusive.

for j in range(11):
    a.append (j)
    b.append(10 - j)

print("a =", a)
print("b =", b)
"""
#-----------------Ex58: Python List Creation and Basic Loop Example (chatgpt) -> nu am apucat sa iau titlul :)))
"""
a = []
b = []
c = []

# In Python, range(11)
# generates numbers from
# 0 to 10 inclusive.

for j in range(11):
    a.append(j)
    b.append(10 - j)
    c.append(a[j] + b[j] - 10)
print("a =", a)
print("b =", b)
print("c =", c)
"""
#-----------------Ex59: Pointless equilibrium
"""
a = []
l = 10

for j in range(l + 1):
    a.append(j + (l - j))

print("a1: ",a)

# or a second version:
# Initialize a list
# of length l+1.

l = 10
a = [None] * (l + 1)
print("a2:",a)

for j in range(l + 1):
    a[j] = j + (1 - j)

print("a3:",a)
"""
#-----------------Ex60: Max value from array
"""
a = [2, 3, 4, 5, 9, 8, 3]
l = len(a)

max_val = 0

for k in range(l):
    if a[k] > max_val:
        max_val = a[k]

print(max_val)
"""
#-----------------Ex61:Min value from array
"""
a = [3, 3, 4, 2, 9, 8, 3]
l = len(a)

min_val = a[0]

for k in range(0, l):
    if a[k] < min_val:
        min_val = a[k]

print(min_val)
"""

#-----------------Ex62: Max value above two arrays of the same size
"""
a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
l = len(a)

max_value = 0
max_a = 0
max_b = 0

for k in range(l):
    if a[k] > max_a:
        max_a = a[k]
    if b[k] > max_b:
        max_b = b[k]
    if max_a > max_value:
        max_b = b[k]
    if max_a > max_value:
        max_value = max_a
    if max_b > max_value:
        max_value = max_b

print(max_value)
"""
#-----------------Ex63: Max value above two arrays of different sizes
"""
a = [2, 3, 4, 5, 9, 8, 3]
b = [14, 2, 3, 41, 5, 6, 77]
l = [0, 0]

l[0] = len(a)
l[1] = len(b)

r = l[0]
if l[0] < l[1]:
    r = l[1]

max_value = 0
for k in range(r):
    if k < l[0] and max_value < a[k]:
        max_value = a[k]
    if k < l[1] and max_value < b[k]:
        max_value = b[k]

print(max_value)
"""
#-----------------Ex64: Which is bigger between n and n+1?
"""
a = [2, 3, 4, 5, 9, 8, 3, 8, 3]
l = len(a) - 1
t = ''

for k in range(l):
    if a[k] > a[k + 1]:
        t += '>'
    else:
        t += '<'

print(t)
"""
#-----------------Ex65:Which is bigger between n and n+1? (optimisation)
"""
a = [2, 3, 4, 5, 9, 8, 3, 8, 3]
l = len(a) - 1
t=''
r='<'
for k in range(0,l):
    if a[k] > a[k + 1]:
        r = ">"
    t += r
    r = "<"

print(t)
"""
#-----------------Ex66: Sum two arrays
"""
a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = []
l = len(a) - 1

for k in range(l + 1):
    c.append(a[k] + b[k])

print("c =", c)
"""
#-----------------Ex67: Simple array mapping
"""
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b = [1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1]
c = []

for j in range(11):
    c.append(a[b[j]])

print("c =", c)
"""
#-----------------Ex68: Sum by coordinates(I)
"""
a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = [1, 1, 1, 4, 4, 4, 6]
l = len(a) - 1

for k in range(0, l + 1):
    c[k] = a[c[k]] + b[k]

print("c =", c)
"""
#-----------------Ex69:Sum by coordinates(II)
"""
a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = [1, 1, 1, 4, 4, 4, 6]
l = len(a) - 1
for k in range(l + 1):
    c[k] = a[c[k]] +b[c[k]]
print("c =", c)
"""
#-----------------Ex70: Cutoff  value
"""
a= [2, 3, 4, 5, 9,8,3]
b = [1, 2, 3, 4, 5, 6, 7]
c = [1, 1, 1, 4, 4, 4, 6]
l = len(a) - 1

for k in range(0, l + 1):
    if a[c[k]] + b[c[k]] > 5:
        c[k] = a[c[k]] + b[c[k]]
    else:
        c[k] =0

print("c =", c)
"""
#-----------------Ex71: Swap array elements by pattern
"""
a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = [0, 1, 1, 0, 0, 0, 1]

l = len(a)

for k in range(l):
    if c[k] == 1:
        t = a[k]
        a[k] = b[k]
        b[k] = t

print("a =", a)
print("b =", b)
"""
#-----------------Ex72: Mix array based on pattern
"""
a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = [0, 1, 1, 0, 0, 0, 1]

l = len(a)

for k in range(l):
    if c[k] == 1:
        c[k] = a[k]
    else:
        c[k] = b[k]

print("c =", c)
"""
#-----------------Ex73: Swap array values
"""
a = ["a", "a", "a", "a", "a", "a"]
b = ["b", "b", "b", "b", "b", "b"]

l = len(a) - 1  # last index

for k in range(l + 1):
    t = a[k]
    a[k] = b[k]
    b[k] = t

print("a =", a)
print("b =", b)
"""
#-----------------Ex74:Intermittent value swap
"""
a = ["a", "a", "a", "a", "a", "a"]
b = ["b", "b", "b", "b", "b", "b"]
l = len(a)-1
k = 0
while k <= l:
    k += 1
    t = a[k]
    a[k] = b[k]
    b[k] = t
    k += 1
print("a =", a)
print("b =", b)
"""
#-----------------Ex75:The welding of array values
"""
a = [1, 2, 3, 4, 5, 6, 7]
b = [2, 2, 2, 2, 2, 2, 2]
l = len(a) - 1
k = 0

while k < l:
    k += 1
    a[k] = a[k] + b[k]
    b[k] = a[k]
    k += 1

print("a =", a)
print("b =", b)
"""
#-----------------Ex76:Static modulo-fill up array with modulo values
"""
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b = []

for j in range(11):
    b.append(a[j] % 3)

print("c =", b)
"""
#-----------------Ex77:Dynamic modulo-take a[i] modulo j
"""
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b = []

for j in range(11):
    b.append(a[j] % (j + 1))

print("c =", b)
"""
#-----------------Ex78: Convert a string to an array
"""
a = "0|13|55|56|1|30|123"
b = "5|33|55|90|1|22|127"

aa = a.split("|")
bb = b.split("|")
cc = []

for i in range(len(aa)):
    cc.append(int(aa[i]) + int(bb[i]))

print(cc)
"""
#-----------------Ex79:
