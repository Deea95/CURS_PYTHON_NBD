          a = [
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]
             ]
          d = 0
          n = len(a)
          m = len(a[0])
          i = 0
          for j in range(m):
             d += a[i][j]
             print(a[i][j])
             i += 1
          print('---\n' + str(d))
        n is set to the number of rows (which is 3
        of columns (also 3). The loop, controlled by
        of each element a[i][ j] to the accumulator
        printed in the console using the print functi
        i+=1 statement, which increments the value o
        (“---\n”) followed by the accumulated sum d