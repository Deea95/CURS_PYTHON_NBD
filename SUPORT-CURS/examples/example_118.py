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
               c[i].append(a[i][j] + b[i][j])
               r += str(c[i][j]) + " "
          print(r)
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
          c = [[0] * len(a[0]) for _ in range(len
          r = ""
          for i in range(len(a)):
            r += "\n"
            for j in range(len(a[i])):
               c[i][j] = a[i][j] + b[i][j]
               r += str(c[i][j]) + " "
          print(r)
        of elements for c, to be immediately accessib
        when needed (.append).