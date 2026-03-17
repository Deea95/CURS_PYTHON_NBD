# 5.1.12Ex. (52) – Traverse a 1D array using a for loop
A = ["a", "b", "c", "d", "e"]

t = ""

for i in range(len(A)):
    t += "\n A[" + str(i) + "]=" + A[i]

print(t)
