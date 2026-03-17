# 7.1.15 Ex. (109) – Show top – right part of the matrix
a = [Output:
[1, 2, 3, 4],
[5, 6, 7, 8], 1
2
3
4
[9, 0, 1, 2], 6
7
8
[3, 4, 5, 6]
1
2
]                             6
d = []
n = len(a)
'''                     
m = len(a[0])                                           
r = ''                          - 6 7 8                 
for i in range(n):              - - - 6                 
# Initializing the inner     '''
# list with None values.
d.append([None] * m)
for j in range(i, m):
    d[i][j] = a[i][j]
    r += str(d[i][j]) + ' '
r += '\n'
print(r)
