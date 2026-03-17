# 5.1.11Ex. (51) – Traverse a 1D array using a while loop (II)
A = ["a", "b", "c", "d", "e", "f", "g"]
Output:
i = 0
i[0] = g
t = ''
i[2] = e
i[4] = c
while i < len(A):
    i[6] = a
t += "\n i[" + str(i) + " ]=" + A[len(A) - i - 1]
i += 2
print(t)
