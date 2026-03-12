           a = [2, 3, 4, 5, 9, 8, 3]
           b = [1, 2, 3, 4, 5, 6, 7]
           c = [0, 1, 1, 0, 0, 0, 1]
           l = len(a)
           for k in range(l):
              if c[k ] ==1 :
                c[k ] =a[ k]
              else:
                c[k ] =b[ k]
           print("c =", c)
        array contains [1, 2, 3, 4, 5, 6, 7]. Additiona
        1, 1, 0, 0, 0, 1]. The goal is to create a new
        0 to the length of the arrays (l), and at each i
        in the c array (c[k]). If c[k] is equal to 1, it
        index k to c[k]. After the loop completes, the