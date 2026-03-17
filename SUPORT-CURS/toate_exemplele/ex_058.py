# 5.1.18Ex. (58) – Insert ascending and descending integer values into arrays
a = []
Output:
b = []
a = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# range(11) to include 10, b = 10,9,8,7,6,5,4,3,2,1,0
# since range in Python is
# upper-bound exclusive.
for j in range(11):
    a.append(j)
    b.append(10 - j)
print("a =", a)
print("b =", b)
