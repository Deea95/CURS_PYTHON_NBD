           a = [2, 3, 4, 5, 9, 8, 3]
           b = [1, 2, 3, 4, 5, 6, 7]
           c = [0, 1, 1, 0, 0, 0, 1]
           l = len(a)
           for k in range(l):
              t = 0
              if c[k ] ==1 :
                t = a[k]
                a[k ] =b[ k]
                b[k ] =t
           print("a =", a)
           print("b =", b)
        This variable will be used for temporarily st
        if statement checks if the value of c[k] is equ
        the values of a[k ] andb [k] are swapped us
        5 Dynamically Resizable Arrays (Lists)