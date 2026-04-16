A=[ ["a", 88, 146], ["b", 34, 124], ["c", 96, 564], [100, 12, "d"], ]
t = "" 
n = len(A) # rows 
m = len(A[0])

i = 0 
j = 0 
for v in range(n * m):
    j = v % m
    if v != 0 and j == 0:
        i += 1
    t += f"{v} A[{i}][{j}]={A[i][j]}\n"
    
print(t)