            a = [
              [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
              [1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
              [1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
              [1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
              [1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
              ]
            b = [
              [1, 0], # right side.
              [-1, 0], # left side.
              [0, 1], # upward side.
              [0, -1], # downward side.
              [1, 1], # upward-right side.
              [-1,-1], # downward-left side.
              [1, -1], # downward-right side.
              [-1, 1] # upward-left side.
              ]
            q = ['*', '#', '%', '&']
            p = []
            def d(a, i, j, n, m, c):
              if i<0 or j<0 or i>=n or \
              j>=m or a[i][j]!=1:
              if a[i][j] == 1:
                a[i][j] = q[c-1]
                p[c - 1] += 1
                for k in b:
                   d(a, i+k[0], j+k[1],n,m,
           def SCAN(a):
              n = len(a) # row.
              m = len(a[0]) # col.
              c = 0   # islands.
              for i in range(n):
                for j in range(m):
                   if a[i][j] == 1:
                     c += 1
                     p.append(0)
                     d(a, i, j, n, m, c)
           def SMC(m):
              r = "\n"
              for row in m:
                for element in row:
                   r += str(element) + " "
                r += "\n"
           print("Islands =", SCAN(a))
           print(SMC(a))
           print(p)
        calculates the size of each island and prints
        directions (up, down, left, right, and diagon
        array q containing characters (“*”, “#”, “%”
        code then prints the following: (i) The num
        calculated by the SCAN function. (ii) The g
        from the q array. (iii) An array p containing
        three main functions as before. Function d(
        (i, j), grid dimensions (n, m), and an islan
        bounds or not part of an island (1 indicates la