# 8.3.1 Ex. (146) – Replacement for repeat loops with recursion
# replacement for                  Output:
# repeat loops.
def for_loop(a, b, r):
    a += 1
    # do stuff from
    r += 5
    # to here
    if a >= b:
        return r
    else:
        return for_loop(a, b, r)


a = for_loop(0, 7, 0)
print(a)
