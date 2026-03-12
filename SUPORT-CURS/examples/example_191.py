def bs(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]: # sw
            t = a[j]
            a = [4, 5, 8, 1, 1, 5, 2, 9]
            print(bs(a))
            # or a second version:
                def bs(a):
                    n = len(a)
                    for i in range(n-1):
                        for j in range(n-i-1):
                            if a[j] > a[j+1]: # swap
                            a = [4, 5, 8, 1, 1, 5, 2, 9]
                            print(bs(a))