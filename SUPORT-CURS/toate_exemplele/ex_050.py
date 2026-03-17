# 5.1.10Ex. (50) – Traverse a 1D array using a while loop (I)
A = ["a", "b", "c", "d", "e", "f", "g"]

i = 0
t = ''

while i < len(A):
    t += "\n i[" + str(i) + "]=" + A[i]
    i += 1

print(t)
