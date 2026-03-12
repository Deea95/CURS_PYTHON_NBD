           a = [2, 3, 4, 5, 9, 8, 3]
           b = [14, 2, 3, 41, 5, 6, 77]
           l = [0, 0]
           l[0] = l en(a)
           l[1] = l en(b)
           r = l[0]
           if l[0] < l [1]:
              r = l[1]
           max_value = 0
           for k in range(r):
              if k < l[0] and max_value < a[k]:
                max_value = a[k]
              if k < l[1] and max_value < b[k]:
                max_value = b[k]
           print(max_value)
        of array a, and l[1] stores the length of arra
        value) to the output. In essence, this code fin