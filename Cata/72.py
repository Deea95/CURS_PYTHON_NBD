a=[2, 3, 4, 5, 9, 8, 3]
b =[1, 2, 3, 4, 5, 6, 7]
c=[0, 1, 1, 0, 0, 0, 1]
l = len(a)

for k in range(l): 
    t = 0 
    if c[k]== 1: 
        t = a[k] 
        a[k]= b[k] 
        b[k]= t 
        
print("a =", a) 
print("b =", b)