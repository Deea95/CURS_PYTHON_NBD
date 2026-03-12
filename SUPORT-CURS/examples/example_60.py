           a = []              Outp
           l = 10
                               a =
           for j in range(l + 1):
              a.append(j + (l - j))
           print(a)
           l = 10
           a = [None ] * (l + 1)
           for j in range(l + 1):
              a[j ] =j + (l - j)
           print(a)
        is, l + 1). During each iteration of the loop, a
        j holds the sum of j and (l−j). The resulting
        10, 10, 10, 10]. In this case, all elements of t
        each iteration calculates j + (l−j), and sinc
        5 Dynamically Resizable Arrays (Lists)