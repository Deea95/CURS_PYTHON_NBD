def smc(m):
    r = ''
    for row in m:
        for val in row:
            a = [5, 2, 8, 4, 6, 12, 8, 9]
            m = 10
            n = len(a)
            max_value = max(a)
            t = [['' for _ in range(n)] for _ in
            for j in range(m):
                for i in range(n):
                    f = (m * a[i]) // max_value
                    # Light shade character.
                    if j < f:
                        # Dark shade character.
                        print(smc(t))