'''
def alpha(c):
    a=[]
    t=list(c)
    k=len(t)

    for i in range(k):
        q=1
        for j in range(len(a)):
            if t[i]==a[j]:
                q=0
        if q==1:
            a.append(t[i])
    return a

print(alpha('uiuhd87trdu645w6575r4i68'))
'''


'''
c = [
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0,1,15,1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
    ]

def matrix_alphabet(t):
    a = []
    n = len(t)
    m = len(t[0])

    for i in range(n):
        for j in range(m):
            q = 1
            for k in range(len(a) + 1):
                if k < len(a) and t[i][j] == a[k]:
                    q = 0
            if q == 1:
                a.append(t[i][j])

    return a

print(matrix_alphabet(c))

'''
'''
a={}
b=[3,6,2,78,99,1,4]

r=0
n=len(b)

for i in range(n):
    a[b[i]]=b[i]

m=max(a.keys())+1

for j in range(m):
    if j in a:
        b[r]=a[j]
        r+=1
print(b)
'''
'''
def p(a):
    max_value=max(a)
    n=len(a)
    m=100

    t=['']*n
    for i in range(n):
        t[i]=str(round((m/max_value)*a[i]))+'%'

    return t

a = [5, 1, 8, 4, 6, 2, 9, 8]
print(p(a))

# or another version:

def p(a):
    max_value = max (a)
    n = len(a)
    m = 100
    t = []

    for i in range(n):
        t.append(str(round((m/max_value)*a[i]))+'%')

    return t

a = [5, 1, 8, 4, 6, 2, 9, 8]
print(p(a))
'''

def p(a,b):
    n=len(a)
    m=[0,0]

    for i in range(n):
        m[0]+=a[i]
        m[1]+=b[i]

    m[0]=m[0]/n
    m[1]=m[1]/n

    s0=0
    s1=0
    s2=0

    for i in range(n):
        s0 += (a[i]-m[0])*(b[i]-m[1])
        s1 += (a[i]-m[0])**2
        s2 += (b[i]-m[1])**2
    r=s0/(s1*s2) **0.05
    return r
a = [6,8,10]
b=[12,10,20]

print(p(a,b))