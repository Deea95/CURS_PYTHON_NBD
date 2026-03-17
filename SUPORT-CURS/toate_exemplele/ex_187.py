# 10.4.6 Ex. (187) – Alphabet detection
# ALPHABET DETECTION.           Output:
def alpha(c):                   u, i, h, d, 8, 7, w, q, s, a


a = []
t = list(c)
k = len(t)
for i in range(k):
    q = 1
    for j in range(len(a)):
        if t[i] == a[j]:
            q = 0
    if q == 1:
        a.append(t[i])
return a
print(alpha('uiuhd87wqsaidhsad'))
