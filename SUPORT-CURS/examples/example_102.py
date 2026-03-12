          m = [
             [2, 4, 4],
             [3, 5, 6],
             [3, 5, 4]
             ]
          a = [[1 for _ in range(len(m[0]))], \
             [1 for _ in range(len(m))]]
          for i in range(len(m)):
             for j in range(len(m[i])):
               # Check if the element
               # exists, if not
               # if not a[0][j]: a[0][j] = 1
               # if not a[1][i]: a[1][i] = 1
               a[0][j ] *=m[i][j]
               a[1][i ] *=m[ i][j]
               # if not a[0][j]: a[0][j] = 0
               # if not a[1][i]: a[1][i] = 0
               # a[0][j] += m[i][j]
               # a[1][i] += m[i][j]
          print('C =', a[0])
          print('R =', a[1])
          m = [
            [2, 4, 4],
            [3, 5, 6],
            [3, 5, 4]
            ]
          a = [[1] * len(m[0]), [1] * len(m)]
          for i in range(len(m)):
            for j in range(len(m[i])):
               a[0][j] *= m[i][j]
               a[1][i] *= m[i][j]
          print('C = ' + str(a[0]))
          print('R = ' + str(a[1]))
        and columns (C). The code then enters a n
        in a[0][ j ] ora [1][i] does not exist (i.e., it is
        tion ensures that if the element is accessed f
        instead of multiplication (“*=”), or initializin