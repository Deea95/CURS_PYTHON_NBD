            def load(c):
              n = c.split('|')
              m = []
              for i in n:
                m.append([int(x) for x in i.
            def SMC(m):
              r = ""
              for row in m:
                for item in row:
                   r += str(item) + ps(item
                r += "\n"
            def ps(a, s):
              t = ""
              b = s - (len(str(a)) % s)
              for _ in range(b):
                t += " "
            c1 = '12,2,44,1,0|34,5,6,7,8|' + \
           c2 = '66,5,45,10,10|37,50,60,17,18|'
           m1 = load(c1)
           m2 = load(c2)
           sm = []
           print(SMC(m1))
           print(SMC(m2))
           for i in range(len(m1)):
              sm.append([])
              for j in range(len(m1[i])):
                sm[i].append(m1[i][j] + m2[i
           print(SMC(sm))
        the sum of the two matrices. The print funct