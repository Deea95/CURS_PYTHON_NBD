          m = [
             [2, 4, 4],
             [3, 5, 6],
             [3, 5, 4]
             ]
          r = []
          for i in range(len(m)):
             # Initialize r[i] to 0.
             r.append(0)
             for j in range(len(m[i])):
               r[i] += m[i][j]
          print(r)
        the outer loop, a variable r[i] is initialized t
        in row i by accumulating the values of m[i][ j
        r where each element r[i] represents the sum
        the “*=” operator, however in this case, usi
        values to calculate the sum (as intended). Ne
        to display the calculated sums for each row