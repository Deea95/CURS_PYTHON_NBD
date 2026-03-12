           def smooth(a):
              n = len(a)
              for i in range(1, n - 1):
                a[i] = (a[i-1] + a[i+1]) / 2
           a = [5, 1, 8, 4, 6, 2, 9, 8]
           print(smooth(a))
        element (index 1) and ends at the second-to-
        the smooth function and prints the returned a