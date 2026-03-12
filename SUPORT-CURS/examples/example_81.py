           a = [5, 1, 8, 4, 6, 2, 9, 8]
           n = len(a)
           max_value = 0
           m = 100
           t = []
           for i in range(n):
              if a[i] > max_value:
                max_value = a[i]
           for i in range(n):
              p = (m / max_value) * a [i]
              print(f'{p}%')
        element a[i] is greater than the current ma
        value variable is updated to the value of a[i
        by the ratio of the current element a[i] to th
        code prints out the calculated p value follow
        5 Dynamically Resizable Arrays (Lists)