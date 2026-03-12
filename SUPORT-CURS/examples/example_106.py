          a = [
             [1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 0, 1, 2],
             [3, 4, 5, 6]
             ]
          d = [0, 0]
          n = len(a)
          m = len(a[0])
          for i in range(n):
             for j in range(m):
               if i == j:
                 d[0] += a[i][j]
               if i + j == n - 1:
                 d[1] += a[i][j]
          print('L=' + str(d[0]) + '|R=' + str(d[
        are the same (i = j), and the secondary diag
        1). The variable n is set to the number of row
        diagonal or the secondary diagonal. If i (the
        column index), the element belongs to the p
        d[0]. This operation accumulates the sum o
        (i + j ) is equal to n( − 1), the element belo
        is added to d[1]. This operation accumulate
        diagonal. Next, the code prints a string that
        the elements on the principal diagonal (L) an
        diagonal (R) in the format “L=value|R=value