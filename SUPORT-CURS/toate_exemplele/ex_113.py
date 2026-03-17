# 7.1.19 Ex. (113) – Secondary diagonal scan (left)
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2], 4
    [3, 4, 5, 6]                  8 3
]
2
7
2
# Initialize the empty list d,
# and define n and m.
d = []
n = len(a)
1
2
3
4
m = len(a[0]) - 6
7
8
r = '' - - 1
2
for i in range(n):
    d.append([])
    '''                     
for j in range(i + 1):                               
  d[i].append(a[i - j][n-1-j])                       
  r += str(d[i][j]) + ' '                            
r += '\n'                                            
print(r)
