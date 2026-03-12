          m = [
            [2, 4, 6],
            [3, 5, 6],
            [3, 5, 4]
            ]
          i = j = 0
          n1 = len(m)
          n2 = len(m[0])
          q = n1 * n2
          for v in range(q):
            j = v % n2
            if j==0 and v!=0 and i<n1 and v!=q:
               i += 1
            print("m[{}][{}]={}".format(i,j,m[i]
        columns, respectively). The variable q is cal
        0 (indicating a new row) and v is not 0 (to
        less than n1 (indicating there are more rows
        matrix. Next, a print statement is used to di
        current indices i and j in the format "m["+i+