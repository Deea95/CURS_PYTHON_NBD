# 10.1.3 Ex. (167) – A 2D array loaded from string
def SMC(matrix):

    result = ""
    for row in matrix:
        for item in row:
            result += item + " "
        result += "\n"
    return result

c = 'AAAAA|BBBBB|CCCCC|DDDDD'
n = c.split('|')

m = [list(row) for row in n]
print(SMC(m))
