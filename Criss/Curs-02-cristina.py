A = ["a", "b", "c", "d", "e", "f", "g"]
i=0
t=''
while i<len(A):
    t += "\n i[" +str(i) +"]=" +A[len(A) -i-1]
    i +=2
print(t)


A = ["a", "b", "c", "d", "e", "f", "g"]
t=''
for i in range(len(A)):
    t += "\n A[" + str(i) + "]=" + A[i]
print (t)

a =["x", "y", 2]
for b in range(len(a)):
    print(a[b])


a=[5,6,8]
b=0
for j in range (len(a)):
    b=b+a[j]
print (b)


a=[5,6,8]
for j in range (len(a)):
    a[j]= 2 * a[j]
print (a)


a=[]
for j in range(11):
    a.append(j)
print(a)


a=[]
b=[]
for j in range(11):
    a.append(j)
    b.append(10-j)
print("a=",a)
print("b=",b)


a=[]
b=[]
for j in range(11):
    a.append(j)
    b.append(10-j)
print("a=",str(a))
print("b=",str(b))


a=[]
b=[]
c=[]
for j in range(11):
    a.append(j)
    b.append(10-j)
    c.append(a[j]+b[j]-10)
print("a=",a)
print("b=",b)
print("c=",c)


a=[]
l=10
for j in range(l+1):
    a.append(j+(l-j))
print("a=",a)


l=10
a= [None]*(l+1)
print (a)


a=[2,3,4,5,9,8,3]
l=len(a)
max_val=0
for k in range(l):
    if a[k]> max_val:
        max_val= a[k]
print(max_val)


a=[3,3,4,2,9,8,3]
l=len(a)
max_val=a[0]
for k in range(l):
    if a[k] < max_val:
        max_val= a[k]
print(max_val)


a=[2,3,4,5,9,8,3]
b=[1,2,3,4,5,6,7]
l=len(a)
max_value=0
max_a=0
max_b=0
for k in range(l):
    if a[k] > max_a:
        max_a= a[k]
    if b[k] > max_b:
        max_b = b[k]
    if max_a > max_value:
        max_value= max_a
    if max_b > max_value:
        max_value= max_b
print(max_value)


a=[2,3,4,5,9,8,3]
b=[14,2,3,41,5,6,77]
l=[0,0]
l[0]=len(a)
l[1]=len(b)
r=l[0]
if l[0] < l[1]:
    r = l[1]
max_value = 0
for k in range(r):
    if k < l[0] and max_value < a[k]:
         max_value= a[k]
    if k < l[1] and max_value < b[k]:
        max_value = b[k]
print(max_value)


a = [2, 3, 4, 5, 9, 8, 3, 8, 3]
l = len(a) - 1
t = ''
for k in range(l):
    if a[k] > a[k + 1]:
        t += '>'
    else:
        t += '<'
print(t)


a = [2, 3, 4, 5, 9, 8, 3, 8, 3]
l = len(a) - 1
t = ''
r = '<'
for k in range(0, l):
    if a[k] > a[k + 1]:
        r = ">"
    t += r
    r = "<"
print(t)


a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = []
l = len(a) - 1
for k in range(l + 1):
    c.append(a[k] + b[k])
print("c =", c)


a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b = [1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1]
c = []
for j in range(11):
    c.append(a[b[j]])
print("c =", c)


a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = [1, 1, 1, 4, 4, 4, 6]
l = len(a) - 1
for k in range(0, l + 1):
    c[k] = a[c[k]] + b[k]
print("c =", c)


a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = [1, 1, 1, 4, 4, 4, 6]
l = len(a) - 1
for k in range(l + 1):
    c[k] = a[c[k]] +b[c[k]]
print("c =", c)


a = [2, 3, 4, 5, 9, 8, 3]
b = [1, 2, 3, 4, 5, 6, 7]
c = [1, 1, 1, 4, 4, 4, 6]
l= len(a) - 1
for k in range(0, l + 1):
    if a[c[k]] + b[c[k]] > 5:
        c[k] = a[c[k]] + b[c[k]]
    else:
        c[k] = 0
print("c =", c)


# a = [2, 3, 4, 5, 9, 8, 3,10,2]
# b = [1, 2, 3, 4, 5, 6, 7]
# c = [0, 1, 1, 0, 0, 0, 1]
# l = len(a)
# for k in range(l):
#     t = 0
#     if c[k] == 1:
#         t = a[k]
#         a[k] = b[k]
#         b[k] = t
# print("a =", a)
# print("b =", b)


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


a = ["a","a","a","a","a","a"]
b = ["b","b", "b","b", "b","b"]
l = len(a) - 1
for k in range(0, l + 1):
    t = a[k]
    a[k] = b[k]
    b[k] = t
print("a =", a)
print("b =", b)


a = ["a","a","a","a","a","a"]
b = ["b","b", "b","b", "b","b"]
c=[1,0,1,0,1,0]
l = len(a) - 1
for k in range(0, l + 1):
    if c[k] == 1:
        t = a[k]
        a[k] = b[k]
        b[k] = t
print("a =", a)
print("b =", b)

a = ["a","a","a","a","a","a"]
b = ["b","b", "b","b", "b","b"]
l = len(a) - 1
k = 0
while k <= 1:
    k += 1
    t = a[k]
    a[k] = b[k]
    b[k] = t
    k += 1
print("a =", a)
print("b =", b)


a = [1, 2, 3, 4, 5, 6, 7]
b = [2, 2, 2, 2, 2, 2, 2]
l = len(a) - 1
k = 0
while k < 1:
    k += 1
    a[k] = a[k] + b[k]
    b[k] = a[k]
    k += 1
print("a =", a)
print("b =", b)


a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b = []
for j in range(11):
    b.append(a[j] % 3)
print("c =", b)


a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b = []
for j in range(11):
    b.append(a[j] % (j+1))
print("c =", b)


a = "0|13|55|56|1|30|123"
b= "5|33|55|90|1|22|127"
aa = a.split("|")
bb = b.split("|")
cc = []
print(aa)
for i in range(len(aa)):
    cc.append(int(aa[i]) + int(bb[i]))
print(cc)


a = "0-13-55-56-1-30-123"
b= "5-33-55-90-1-22-127"
aa = a.split("-")
bb = b.split("-")
cc = []
print(aa)
for i in range(len(aa)):
    cc.append(int(aa[i]) + int(bb[i]))
print(cc)


a = [5, 1, 8, 4, 6, 2, 9, 8]
n = len(a)
max_value = 0
m = 100
t = []
for i in range(n):
    if a[i] > max_value:
        max_value = a[i]
for i in range(n):
    p = (m / max_value) * a[i]
    print(f'{p}%')


a = [5, 6, 2, 9, 44, 200]
n = len(a)
b = 0
e = 0
for j in range(n):
    b += a[j]
x = b / n
for j in range(n):
    e += (a[j] - x) ** 2
s = (e / (n - 1)) ** 0.5
c = s / x
print('AV =', x)
print('SD =', s)
print('CV =', c)


a = [5, 1, 8, 4, 6, 2, 8, 9]
c = '#'
t = ''
n = len(a)
for i in range(n):
    for k in range(a[i]):
        t += c
    t += '\n'
print(t)


a = [5, 2, 8, 4, 6, 22, 8, 9]
m=15
c = '#'
t = ''
max_value = 0
n = len(a)
for i in range(n):
    if a[i] > max_value:
        max_value = a[i]
for i in range(n):
    f = int((m / max_value) * a[i])
    for k in range(f):
        t += c
    t += '\n'
print(t)


a = [5, 2, 8, 4, 6, 22, 8, 9]
m = 15
t = ''
max_value = 0
n = len(a)
for i in range(n):
    if a[i] > max_value:
        max_value = a[i]
for i in range(n):
    f = int((m / max_value) * a[i])
    for k in range(m):
        if k < f:
            t += '▮'
        else:
            t += '▯'
    t += '\n'
print(t)


A = [
["a", 88, 146],
["b", 34, 124],
["c", 96, 564],
[100, 12, "d"],
]
print(A[1][2])
A = [
["a", 88, 146],
["b", 34, 124],
["c", 96, 564],
[100, 12, "d"],
]
t = ""
for i in range(len(A)):
    for j in range(len(A[i])):
        t += "\n A[{}][{}]={}".format(i,j, A[i][j])
print(t)


m = [
[2, 4, 6],
[3, 5, 6],
[3, 5, 4]
]

i = j = 0
n1 = len(m)
n2 = len(m[0])
q = n1 * n2

for v in range(q):
    j = v % n2
    if j == 0 and v != 0 and i<n1 and v != q:
        i += 1
print("m[{}][{}]={}".format(i,j,m[i][j]))


A = [
["a", 88, 146],
["b", 34, 124],
["c", 96, 564],
[100, 12, "d"],
]
t = ""
n = len(A)
m = len(A[0])
i = 0
j = 0
for v in range(n * m):
    j = v % m
    if v != 0 and j == 0:
        i += 1
    t += f"{v} A[{i}][{j}]={A[i][j]}\n"
print(t)


A = [
    [
        ["a", 88, 146],
        ["b", 34, 124],
        ["c", 96, 564],
        [100, 12, "d"],
    ],
    [
        ["e", 48, 996],
        ["f", 34, 554],
        ["g", 26, 884],
        [111, 92, "h"],
    ]
]
print(A[1][2])