m = [
i = j = 0
n1 = len(m)
n2 = len(m[0])
q = n1 * n2
for v in range(q):
    j = v % n2
    if j==0 and v!=0 and i<n1 and v!=q:
        print("m[{}][{}]={}".format(i,j,m[i]