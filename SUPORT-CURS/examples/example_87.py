          A = [
            ["a", 88, 146],
            ["b", 34, 124],
            ["c", 96, 564],
            [100, 12, "d"],
            ]
          t = ""
          for i in range(len(A)):
            for j in range(len(A[i])):
               t += "\n A[{}][{}]={}".format(i,
          print(t)
        It creates a string in the format “A[i][ j] =
        code prints the accumulated string t to the co