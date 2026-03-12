          m = [
             [2, 4, 4],
             [3, 5, 6],
             [3, 5, 4]
             ]
          a = [
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]
             ]
          for i in range(len(m)):
             for j in range(len(m[i])):
               if not a[2][j]:
                 a[2][j] = 10000
               if not a[3][i]:
                 a[3][i] = 10000
               if a[0][j] < m[i][j]:
                 a[0][j] = m[i][j]
               if a[1][i] < m[i][j]:
                 a[1][i] = m[i][j]
               if a[2][j] > m[i][j]:
                 a[2][j] = m[i][j]
               if a[3][i] > m[i][j]:
                 a[3][i] = m[i][j]
          print('C Max =', a[0])
          print('R Max =', a[1])
          print('C Min =', a[2])
          print('R Min =', a[3])
          m = [
            [2, 4, 4],
            [3, 5, 6],
            [3, 5, 4]
            ]
          a = [
            [0, 0, 0],
            [0, 0, 0],
            [10000, 10000, 10000],
            [10000, 10000, 10000]
            ]
          for i in range(len(m)):
            for j in range(len(m[i])):
               a[0][j] = max(a[0][j], m[i][j])
               a[1][i] = max(a[1][i], m[i][j])
               a[2][j] = min(a[2][j], m[i][j])
               a[3][i] = min(a[3][i], m[i][j])
          print('C Max =', a[0])
          print('R Max =', a[1])
          print('C Min =', a[2])
          print('R Min =', a[3])
        first set (a[0][ j ] anda [1][i]) is designed to
        and row of the m matrix. The second set (a[2
        code outputs the results using the print statem
        (1) “C Max” represents the maximum valu
        Max” represents the maximum value for eac
        the minimum value for each column of mat
        value for each row of m. A second version of