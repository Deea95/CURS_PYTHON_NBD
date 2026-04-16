a=[2, 3, 4, 5, 9, 8, 3]
b =[1, 2, 3, 4, 5, 6, 7]
c =[1, 1, 1, 4, 4, 4, 6]
l = len(a)-1 
for k in range(0, l + 1):
    if a[c[k]] + b[c[k]] > 5:
        c[k]=a[c[k]] + b[c[k]]
    else:
        c[k]= 0
        
    
print("c =", c)