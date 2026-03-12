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
                     a.append(t[i][j])
            def decompose(c, a):
               n = len(c)
               m = len(c[0])
               d = []
               for i in range(n):
                 d.append([])
                 for j in range(m):
                   d[i].append([])
                   for k in range(len(a) +
                      d[i][j].append(" ")
                      if k < len(a) and c
                        d[i][j][k ] =c[
           def SMC(m, k):
              r = 'M' + str(k+1)
              r += '\n ----------\n'
              for i in range(len(m)):
                r += "|"
                for j in range(len(m[i])):
                   r += str(m[i][j][k])
                r += "|\n"
              r += ' ----------'
           r = "u"
           c = [
              [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
              [1, 2, 1, 0, 1, 3, 1, 0, 1, 1],
              [1, 1, 2, 0, 1, 3, 0, 1, 0, 1],
              [0, 1, 0, 2, 1, 3, 1, 0, 0, 1],
              [1, 1, 1, 0, 2, 3, 1, 0, 1, 0],
              [1, 0, 1, 1, 1, 3, 0, r, 0, 0],
              [1, 0, 3, 3, 3, 3, r, 0, 0, 1],
              [1, 0, 1, 1, 1, r, 0, 9, 9, 9],
              [1, 1, 0, 0, 0, 0, 1, 9, 0, 9]
              ]
           b = matrix_alphabet(c)
           t = decompose(c, b)
           for k in range(len(b)):
              print(SMC(t, k))
           print(b)
        that matrix. The code also prints the decom
        array b, and for each unique value in b, it
        through the elements of t, checks if each valu
        is surrounded by lines and separators for b
        printing the alphabet array b and the decomp