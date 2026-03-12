           a = []
           b = []
           # range(11) to include 10,
           # since range in Python is
           for j in range(11):
              a.append(j)
              b.append(10 - j)
           print("a =", a)
           print("b =", b)
        5 Dynamically Resizable Arrays (Lists)
        (a.append adds one element at each iteration
        coincides with j) to the current value of j, w
        10. Simultaneously, it sets b[ j ] to the value
        to 0. These assignments continue for each ite
        its execution, it prints the contents of both ar