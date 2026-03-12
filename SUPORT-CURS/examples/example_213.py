a = [
b = [
q = ['*','#','%','&','@','$','!','+'
p = [[], [], []]
def d(a, i, j, n, m, c):
    if i<0 or j<0 or i>(n-1) or \
    for k in range(len(b)):
        def scan(a):
            n = len(a) # row.
            m = len(a[0]) # col.
            c = 0 # islands.
            for i in range(n):
                for j in range(m):
                    if a[i][j] == 1:
                        for i in range(c):
                            def smc(m, f):
                                r = ''
                                for i in range(len(m)):
                                    for j in range(len(m[i])):
                                        def ps(a, f):
                                            t = ''
                                            b = f - (len(a) % f)
                                            for i in range(b):
                                                print('Islands =', scan(a), '\n')
                                                print(smc(a, 1))
                                                print(smc(p, 4))
                                                prints the number of islands found and two
                                                if the current position is within bounds and