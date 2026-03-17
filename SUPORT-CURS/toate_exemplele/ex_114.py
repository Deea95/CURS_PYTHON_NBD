# 7.1.20 Ex. (114) – Show bottom – right and flip horizontally
a = [Output:
[1, 2, 3, 4],
[5, 6, 7, 8], 4
[9, 0, 1, 2], 8
7
[3, 4, 5, 6]
2
1
0
]                             6
5
4
3
d = []
n = len(a)
m = len(a[0])
r = ''
for i in range(n):              3
4
5
6
d.append([])
for j in range(i + 1):       '''                     
               d[i].append(a[i][m-j-1])                           
               r += str(d[i][j]) + ' '                            
             r += '\n'                                            
          print(r)
