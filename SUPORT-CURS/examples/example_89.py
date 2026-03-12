A = [
t = ""
n = len(A) # rows
m = len(A[0]) # columns
i = 0
j = 0
for v in range(n * m):
    j = v % m
    if v != 0 and j == 0:
        print(t)