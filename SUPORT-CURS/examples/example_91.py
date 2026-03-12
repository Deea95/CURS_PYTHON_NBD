A = [
t = ""
s = len(A) # 5 matrices
m = len(A[0]) # 4 rows
n = len(A[0][0]) # 3 columns
i = 0
j = 0
d = 0
k = 0
q = n * m * s
for v in range(q):
    k = v % (m * n)
    j = v % n
    if v != 0 and j == 0:
        if v != 0 and k == 0:
            i = 0
            print(t)