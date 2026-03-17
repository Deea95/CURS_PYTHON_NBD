# 5.1.11Ex. (51) – Traverse a 1D array using a while loop (II)
A = ["a", "b", "c", "d", "e", "f", "g"]

i = 0
t = ''

while i < len(A):
    t += "\n i[" + str(i) + "]=" + A[len(A) - i - 1]
    i += 2
print(t)
