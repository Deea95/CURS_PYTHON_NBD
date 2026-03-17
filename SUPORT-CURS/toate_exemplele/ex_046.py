# 5.1.6Ex. (46) – Changing values in array elements -swap values or replace
A = ["a", "b", "c"]
x = A[1]

A[0] = " d"
A[1] = A[2]
A[2] = x
print(A[0] + A[1] + A[2])
