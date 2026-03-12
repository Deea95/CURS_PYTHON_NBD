# ALPHABET DETECTION.
def alpha(c):
    a = []
    t = list(c)
    k = len(t)
    for i in range(k):
        q = 1
        for j in range(len(a)):
            if t[i] == a[j]:
                q = 0
                if q == 1:
                    print(alpha('uiuhd87wqsaidhsad'))