# 10.5.3 Ex. (191) – An optimized version of Bubble Sort
def bs(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:  # swap.
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t
    return a
a = [4, 5, 8, 1, 1, 5, 2, 9]
print(bs(a))

# or a second version:
def bs(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:  # swap.
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


a = [4, 5, 8, 1, 1, 5, 2, 9]
print(bs(a))
