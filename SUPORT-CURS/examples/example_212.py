a = [
b = [
q = ['*', '#', '%', '&']
p = []
def d(a, i, j, n, m, c):
    if i<0 or j<0 or i>=n or \
    if a[i][j] == 1:
        for k in b:
            def SCAN(a):
                n = len(a) # row.
                m = len(a[0]) # col.
                c = 0 # islands.
                for i in range(n):
                    for j in range(m):
                        if a[i][j] == 1:
                            def SMC(m):
                                r = "\n"
                                for row in m:
                                    for element in row:
                                        print("Islands =", SCAN(a))
                                        print(SMC(a))
                                        print(p)