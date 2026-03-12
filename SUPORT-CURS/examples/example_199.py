            def entropy(c):
              a = alpha(c)
              n = len(a)
              k = len(c)
              e = 0
              for i in range(n):
                r = len(c.replace(a[i], ''))
                a[i ] = (k - r ) /k
                # e += -a[i] * log(2, a[i])
                e += a[i ] *l og(2, 1 / a[i])
            def alpha(c):
              a = []
              t = list(c)
              k = len(t)
              for i in range(k):
                q = 1
                for j in range(len(a)):
                   if t[i] == a[j]:
                     q = 0
                if q == 1:
                   a.append(t[i])
           def log(n, v):
              return math.log(v) / math.log(n)
           print(entropy('uiuhd87wqsaidhsad'))
        responsible for detecting the alphabet (uniqu
        acters (stored in variable n), and the total le
        function initializes variables for entropy e, a
        (represented by a[i]). For each character, i
        character a[i] is then temporarily stored in l
                             ( )
                   e =  p × log  =
                      i=1      i
                   e =−  p × log (p ) =
                       i=1
          The alpha function is responsible for alp
        Log(n, v) that calculates the logarithm of v w
        (unique characters) within it. The result is r
        specific case, it is printed to the console usin
        those between hexadecimal (hex), text, deci
        about encoding characters into binary for dig