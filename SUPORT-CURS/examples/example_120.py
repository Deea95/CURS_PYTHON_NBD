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
          i = j = 0
          r = ""
          c = []
          n1 = len(a)
          n2 = len(a[0])
          q = n1 * n2
          c.append([])
          for v in range(q):
             j = v % n2
             if j==0 and v!=0 and i<n1 and v!=q:
               i += 1
             c.append([])
             r += "\n"
             c[i].append(0)
             for k in range(len(a[i])):
               c[i][j] += a[k][j] * b[i][k]
               r += str(c[i][j]) + " "
          print(r)
        and print the result. Two 2D arrays, a and b,
        n2), denoted as q. The loop variable is v. Wi
        separate rows. The code sets c[i][ j] to 0 to p
        result, c[i][ j], is appended to the r string fo
        The code prints the contents of the r string i