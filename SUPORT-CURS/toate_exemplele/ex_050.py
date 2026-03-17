# 5.1.10Ex. (50) – Traverse a 1D array using a while loop (I)
A = ["a", "b", "c", "d", "e", "f", "g"]
Output:
i = 0
i[0] = a
t = ''
i[1] = b
i[2] = c
while i < len(A):
    i[3] = d
t += "\n i[" + str(i) + " ]=" + A[i]
i[4] = e
i += 1
i[5] = f
i[6] = g
print(t)
