          a = [1, 2, 3, 4, 5]
          t = 0
          def c1(t, a):
             return 5 + c2(t, a)
          def c2(t, a):
             return c3(t, a) + 5
          def c3(t, a):
             s = 1
             return s + c4(t, a)
          def c4(t, a):
             return c5(t, a) + c5(t, a)
          def c5(t, a):
             for i in a:
               t += i
          b = c1(t, a)
          print(b)
        elements [1, 2, 3, 4, 5]. A variable t is initia