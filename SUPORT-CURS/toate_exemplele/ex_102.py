# 7.1.8 Ex. (102) – Multiply all values from the columns / rows and store them in array
m = [
[2, 4, 4],
[3, 5, 6],
[3, 5, 4]

]
# Initialize a with
# default values.
a = [[1 for _ in range(len(m[0]))], \
     [1 for _ in range(len(m))]]
for i in range(len(m)):
    for j in range(len(m[i])):
        # Check if the element
        # exists, if not
        # initialize to 1.
        # In Python, this check
        # is not necessary since
        # we have initialized all
        # elements to 1.
        # if not a[0][j]: a[0][j] = 1
        # if not a[1][i]: a[1][i] = 1
        a[0][j] *= m[i][j]
        a[1][i] *= m[i][j]
        # The commented out code
        # is an alternative
        # calculation, not used in
        # the active code.
        # if not a[0][j]: a[0][j] = 0
        # if not a[1][i]: a[1][i] = 0
        # a[0][j] += m[i][j]
        # a[1][i] += m[i][j]
print('C =', a[0])
print('R =', a[1])
# or another version:
m = [
    [2, 4, 4],
    [3, 5, 6],
    [3, 5, 4]
]
a = [[1] * len(m[0]), [1] * len(m)]
for i in range(len(m)):
    for j in range(len(m[i])):
        a[0][j] *= m[i][j]
        a[1][i] *= m[i][j]
print('C = ' + str(a[0]))
print('R = ' + str(a[1]))
