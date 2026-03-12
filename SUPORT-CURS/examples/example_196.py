            def p(a, b):
              n = len(a)
              m = [0, 0]
              for i in range(n):
                m[0 ] +=a [i]
                m[1 ] +=b [i]
              m[0 ] =m [0 ] /n # mean a.
              m[1 ] =m [1 ] /n # mean b.
              s0 = 0
              s1 = 0
              s2 = 0
              for i in range(n):
                s0 += (a[i ] -m[0]) * (b[i ]
                s1 += (a[i ] -m[0]) ** 2
                s2 += (b[i ] -m[1]) ** 2
              r = s0 / (s1 * s2 ) **0 .5
            a = [6, 8, 10]
            b = [12, 10, 20]
            print(p(a, b))
        all values in b is accumulated in m[1]. These
                             n [(x
                     r = / Σ i=1 i
                          n (x − x)2
                          i=1 i
        (because they are equal). The formula for r
                             r =
                s0 = [(x − x)(y − y)] =
                   i=1           i
                [         [
             s1 = | (x − x)2 = | (a[i] −
                 i=1        i=0
                [         [
             s2 = | (y − y)2 = | (b[i] −
                 i=1        i=0
        the p function, and then is printed in the o
        (perfect negative correlation) to 1 (perfect po