def SMC(matrix):
    result = ""
    for row in matrix:
        for item in row:
            c = 'AAAAA|BBBBB|CCCCC|DDDDD'
            n = c.split('|')
            m = [list(row) for row in n]
            print(SMC(m))
            c = “AAAAA|BBBB