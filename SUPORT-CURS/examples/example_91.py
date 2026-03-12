          A = [
            [
               ["a", 55, 146],
               ["b", 34, 124],
               ["c", 96, 564],
               [100, 12, "d"],
            ],
            [
               ["e", 88, 146],
               ["f", 34, 124],
               ["g", 96, 564],
               [100, 12, "h"],
            ],
            [
               ["i", 88, 146],
               ["j", 34, 124],
               ["k", 96, 564],
               [100, 12, "k"],
            ],
            [
               ["m", 88, 146],
               ["n", 34, 124],
               ["o", 96, 564],
               [100, 12, "p"],
            ],
            [
               ["q", 88, 146],
               ["r", 34, 124],
               ["s", 96, 564],
               [100, 12, "t"],
            ]
          ]
          t = ""
          s = len(A) # 5 matrices
          m = len(A[0]) # 4 rows
          n = len(A[0][0]) # 3 columns
          i = 0
          j = 0
          d = 0
          k = 0
          q = n * m * s
          for v in range(q):
            k = v % (m * n)
            j = v % n
            if v != 0 and j == 0:
               i += 1
            if v != 0 and k == 0:
               i = 0
               d += 1
            t += str(v ) +" A[" + str(d ) + \
               "][" + str(i ) +" ][" + str(j )
            t += str(A[d][i][j]) + "\n"
          print(t)
        value” for each element in the array, where v