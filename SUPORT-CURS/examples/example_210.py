def matrix_alphabet(t):
    a = []
    n = len(t)
    m = len(t[0])
    for i in range(n):
        for j in range(m):
            q = 1
            for k in range(len(a) +
            if k < len(a) and t[
            q = 0
            if q == 1:
                def decompose(c, a):
                    n = len(c)
                    m = len(c[0])
                    d = []
                    for i in range(n):
                        for j in range(m):
                            for k in range(len(a) +
                            if k < len(a) and c
                            def SMC(m, k):
                                r = 'M' + str(k+1)
                                for i in range(len(m)):
                                    for j in range(len(m[i])):
                                        # Main code
                                        r = "u"
                                        c = [
                                        b = matrix_alphabet(c)
                                        t = decompose(c, b)
                                        for k in range(len(b)):
                                            print(SMC(t, k))
                                            print(b)
                                            printing the alphabet array b and the decomp