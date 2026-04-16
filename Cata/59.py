a = []
b = []
c = []

for j in range(11): 
    a.append(j) 
    b.append(10-j) 
    c.append(a[j]+ b[j]-10) 

print("a =", a) 
print("b =", b) 
print("c =", c)