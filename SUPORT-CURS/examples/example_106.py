# Sum on principal and secondary diagon
a = [
d = [0, 0]
n = len(a)
m = len(a[0])
for i in range(n):
    for j in range(m):
        if i == j:
            if i + j == n - 1:
                print('L=' + str(d[0]) + '|R=' + str(d[