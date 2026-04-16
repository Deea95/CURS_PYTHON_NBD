a =[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] 
b =[] 
for j in range(11):
    b.append(a[j]%(j + 1)) 
    
print("c =", b)