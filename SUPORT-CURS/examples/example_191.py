def bs(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:  # sw
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t


a = [4, 5, 8, 1, 1, 5, 2, 9]
print(bs(a))


def bs(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:  # swap
                a[j], a[j + 1] = a[j + 1]


a = [4, 5, 8, 1, 1, 5, 2, 9]
print(bs(a))
