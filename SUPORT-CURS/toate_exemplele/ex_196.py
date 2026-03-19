def p(a, b):
    n = len(a)
    m = [0, 0]

    # calcul medii
    for i in range(n):
        m[0] += a[i]
        m[1] += b[i]

    m[0] = m[0] / n  # mean a
    m[1] = m[1] / n  # mean b

    s0 = 0
    s1 = 0
    s2 = 0

    # calcul coeficient
    for i in range(n):
        s0 += (a[i] - m[0]) * (b[i] - m[1])
        s1 += (a[i] - m[0]) ** 2
        s2 += (b[i] - m[1]) ** 2

    r = s0 / (s1 * s2) ** 0.5
    return r


a = [6, 8, 10]
b = [12, 10, 20]

print(p(a, b))