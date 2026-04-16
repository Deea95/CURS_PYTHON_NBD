def p(a):
    max_value = max(a)
    n = len(a)
    m = 100

    # Preaallocate the list
    # with the required size.

    t = [''] * n
    for i in range(n):
        t[i] = str(round((m / max_value) * a[i]))+ '%'

    return t


......

