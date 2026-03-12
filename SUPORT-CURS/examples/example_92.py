# integer division 2D one-for loop
# no if then involved.
A = [
t = ""
n = len(A) # rows
m = len(A[0]) # columns
for k in range(n * m):
    j = k % m
    i = k // m
    print(t)