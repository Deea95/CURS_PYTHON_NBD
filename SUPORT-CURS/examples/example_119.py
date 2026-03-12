          a = [
             [2, 4, 6],
             [3, 5, 6],
             [3, 5, 4]
             ]
          b = [
             [2, 4, 6],
             [3, 5, 6],
             [3, 5, 4]
             ]
          c = []
          r = ""
          for i in range(len(a)):
             r += "\n"
             c.append([])
             for j in range(len(a[i])):
               c[i].append(0)
               for k in range(len(a[i])):
                 c[i][j] += a[k][j] * b[i][k
               r += str(c[i][j]) + " "
          print(r)
        nested for loops to iterate through the rows
        k, is responsible for performing the matrix m