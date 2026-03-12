def p(a):
    max_value = max(a)
    n = len(a)
    m = 100
    # Preallocate the list
    # with the required size.
    t = [''] * n
    for i in range(n):
        a = [5, 1, 8, 4, 6, 2, 9, 8]
        print(p(a))
        # or another version:
            def p(a):
                max_value = max(a)
                n = len(a)
                m = 100
                t = []
                for i in range(n):
                    a = [5, 1, 8, 4, 6, 2, 9, 8]
                    print(p(a))