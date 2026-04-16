a=["a", "a", "a", "a", "a", "a"]
b =["b", "b", "b", "b", "b", "b"]

l = len(a)-1
k = 0 

while k <= l: 
    k += 1
    t = a[k]
    a[k]= b[k] 
    b[k]= t
    k += 1 
    
print("a =", a)
print("b =", b)