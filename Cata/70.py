a=[2, 3, 4, 5, 9, 8, 3]
b =[1, 2, 3, 4, 5, 6, 7]
c =[1, 1, 1, 4, 4, 4, 6]
l = len(a)-1 
for k in range(l + 1): 
    c[k]= a[c[k]] + b[c[k]]
        
    
print("c =", c)