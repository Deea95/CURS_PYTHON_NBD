            c = [
              [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
              [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
              [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
              [0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
              [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
              [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
              ]
            def matrix_alphabet(t):
              a = []
              n = len(t)
              m = len(t[0])
              for i in range(n):
                for j in range(m):
                   q = 1
                   for k in range(len(a) +
                     if k < len(a) and t[
                       q = 0
                   if q == 1:
                     a.append(t[i][j])
            print(matrix_alphabet(c))
        0 or 1) that likely can represent some sort o
        range of applications, from data organizatio
        its core, sorting involves the arrangement o
        as efficiently organized data allows for faster