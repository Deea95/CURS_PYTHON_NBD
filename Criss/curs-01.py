a=3
b=a
print(b)


a=3
b=2
c=a + b / 2 - a * b
print(c)


a=3
a=a % 2
print(a)


a=2
a=a+1
print(a)


a=2
a+=1
print(a)


a = 2;
a = a + a;
print(a);


a = 2
a = a - a
a=a - 1
print(a)


a = 2
a += a - 1
a += a - 1
print(a)


a = 3
b=7
t=0

t=a
a=b
b=t
print('a=', b)
print('b=', t)


a=3
b=a+7
a= None
print(a)
print(b)


s   =(1+2+3+
   4+5+6+7+8)
print (s)


a=3
b=7
c=10
r = "a = " + str(a) + " and b = " + str(b)
t = " is a number.\n"
l = str(a+b/c)+t
print(l+r)


a=4
b=7
if a < b:
    print(a)
else:
    print(b)


a=2
b=3
c=1

if a < b:
    c=0
print(c)


a=1
b=2
c=3

if a < b:
    c+=1
else:
    c-=1

print("c=" + str(c))


a=1
b=2
c=3

if a < b:
    c-=1
elif b==c:
    c+=1
else:
    c=0

print("c=" + str(c))


a=1
b=0

if a ==0:
    b =11
elif a ==1:
    b=64
elif a ==2:
    b=33

print(b)


i=0

while i<5:
    print("i = ", i)
    i=i+1


i=0

while True:
    print("i = " + str (i))
    i+=1
    if i>=5:
        break


for i in range(5):
    print(5-i)


for i in range(10, 5, -1):
    print(i)


i=10
while i>5:
    i -=1
    print(i)
    i-=1


a=5

for i in range(a):
    print(a-i)


a=0

for i in range(1,6):
    a=a+(i+4*3)

print(a)


a=0

for i in range(11):
    a=a+i

print(a)


r=0

for i in range(10):
    for j in range(10):
        r+=1

print(r)


r=0

for i in range(4):
    for j in range(4):
        r+=3

print(r)


r=0

for i in range(10):
    for j in range(10):
        r+=j*i

print(r)


a=0
m=3
n=5

for j in range(1, m+1):
    for i in range(1, n+1):
        a= a+(i+j*3)

print(a)


a=0

for j in range(1, 4):
    for i in range(1, 6):
        a= a+(i+3)

print(a)


a=0
m=3
n=5

for j in range(1, m+1):
    for i in range(1, n+1):
        a= a+(i+j*m)

print(a)


a=0
m=4

for j in range(1, m+1):
    for i in range(1, j+1):
        a= a+(i+j*m)

print(a)


a=0
m=5
n=7

for j in range(1, m+1):
    for i in range(j, n+1):
        a+= (i+j*m)

print(a)


a=0
m=4

for i in range(2):
    for j in range(3):
        print(f"i = {i}, j = {j}")


i=j=0
n1=2
n2=3
q=n1*n2
for v in range(q):
    j = v % n2
    if j == 0 and v != 0 and i < n1 and v != q:
        i += 1
    print(f"i = {i}, j = {j}")


i=j=0
n1=2
n2=3
q=n1*n2
for v in range(q):
    j = v % n2
    if j == 0 and v != 0 and i < n1 and v != q:
        i += 1
    print(f"i = {i}, j = {j}")


a=[2,5,7]
b=[6,8]

print(a+b)


a=[2,5,7]
b=[6,8]
c=a[1]+b[0]
print(c)


A = []
A.append("a")
A.append("b")
A.append("c")

print (A[0] +A [1] + A[2])


A = []
B = []

A = ["a", "b", "c"]
B = [1,2,3]

print (A[0] +A[1] + A[2])
print (B[0] +B[1] + B[2])


A = ["a", "b", "c"]

x=A[1]
y=A[2]

print (x+y)


A = ["a", "b", "c"]

x=A[1]

A[0]="d"
A[1] = A[2]
A[2] = x

print (A[0] +A[1] + A[2])


a = [2,5,7]
b=[6,8]

a[1]-=1
b[0]-=1

c=a[1]+b[0]

print (c)


a = [5,6,8]
b=len(a)

print (b)


A= [1,2,3]

if A[0] <A[1]:
    A[2]+=1

print ("A[2]=" + str(A[2]))


A = ["a", "b", "c","d", "e", "f", "g"]

i=0
t=''

while i<len(A):
    t+="\n i[" + str(i) +"]=" +A[i]
    i+=1
print (t)