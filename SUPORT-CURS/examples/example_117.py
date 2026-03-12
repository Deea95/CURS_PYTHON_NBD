a = [
b = [
n = len(a)
m = len(a[0])
r = 0
for i in range(n):
    for j in range(m):
        if b[i][j] == 1:
            print(r)