# 10.1.3 Ex. (167) – A 2D array loaded from string
def SMC(matrix):                 Output:


result = ""
for row in matrix:             A
A
A
A
A
for item in row:             B
B
B
B
B
result += item + " "
C
C
C
C
C
result += "\n"
D
D
D
D
D
return result
c = 'AAAAA|BBBBB|CCCCC|DDDDD'
n = c.split('|')
m = [list(row) for row in n]
print(SMC(m))
