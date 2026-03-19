a = []


def permute(s, r, l):
    if l == r:
        a.append(s)
    else:
        for i in range(l, r + 1):
            s = swap(s, l, i)
            permute(s, r, l + 1)
            s = swap(s, l, i)


def swap(s, i, j):
    c = list(s)
    t = c[i]
    c[i] = c[j]
    c[j] = t
    return ''.join(c)


s = "ACTG"
n = len(s)
permute(s, n - 1, 0)
print(a)
that
takes
three
arguments: s(the
string
to
be
