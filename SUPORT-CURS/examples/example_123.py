          def SMC(m):
             r = "\n"
             for i in range(len(m)):
               for j in range(len(m[i])):
                  r += " " + str(m[i][j]) +
               r += "\n"
          a = [
             [2, 2, 2, 2, 2],
             [2, 2, 2, 2, 2],
             [2, 2, 2, 2, 2],
             [2, 2, 2, 2, 2],
             [2, 2, 2, 2, 2]
             ]
          b = [
             [1, 1, 0, 0, 0],
             [3, 1, 0, 0, 1],
             [1, 3, 0, 1, 1],
             [0, 0, 0, 7, 0],
             [3, 0, 4, 0, 9]
             ]
          c = [
             [3, 3, 3, 3, 3],
             [3, 3, 3, 3, 3],
             [3, 3, 3, 3, 3],
             [3, 3, 3, 3, 3],
             [3, 3, 3, 3, 1]
             ]
          n = len(a)
          m = len(a[0])
          for i in range(n):
             for j in range(m):
               if b[i][j ] ==0 :
                  c[i][j ] =a [i][j ] *c [i][j
               elif b[i][j ] ==1:
                  c[i][j ] =a [i][j ] +c[i][j
               elif b[i][j ] ==2:
                  c[i][j ] =a [i][j ] -c[i][j
               elif b[i][j ] ==3:
                  c[i][j ] =c [i][j ] -a[i][j
               elif b[i][j ] ==4:
                  c[i][j ] =a [i][j ] %c[i][j
               elif b[i][j ] ==5:
                  c[i][j ] =a [i][j ] /c[i][j
               elif b[i][j ] ==6:
                  c[i][j ] =a [i][j]
               elif b[i][j ] ==7:
                  c[i][j ] =' #'
               elif b[i][j ] ==8:
                  pass # Placeholder for "d
               elif b[i][j ] ==9:
                  if c[i][j ] <=a[i][j]:
                    c[i][j ] =a[i][j]
          print(SMC(c))