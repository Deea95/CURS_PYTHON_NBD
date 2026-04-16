def for_loop(a, b, r):
    a += 1
    r += 5
    if a >= b:
        return r
    else:
        return for_loop(a, b, r)


a = for_loop(0, 7, 0)
print(a)
