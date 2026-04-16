
b =['a', 'b', 'c', 'd', 'e', 'f']
n = len(b) 
c =[None]* n 

for i in range(n):
    c[i]= b[n-i-1] 
    
print(c)