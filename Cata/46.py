A=["a", "b", "c"] 
x = A[1] 
A[0]= "d" 
A[1]= A[2] 
A[2]= x 
print(A[0]+ A[1]+ A[2])