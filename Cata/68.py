a=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] 
b =[1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1] 
c =[] 
for j in range(11): 
    c.append(a[b[j]]) 
print("c =", c)