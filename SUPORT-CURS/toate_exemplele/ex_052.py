# 5.1.12Ex. (52) – Traverse a 1D array using a for loop
A = ["a", "b", "c", "d", "e"]
Output:
t = ""
A[0] = a
A[1] = b
for i in range(len(A)):            A[2] = c
t += "\n A[" + str(i) + "]=" + A[i]
A[3] = d
A[4] = e
print(t)
