a = [
b = [
i = j = 0
r = ""
c = []
n1 = len(a)
n2 = len(a[0])
q = n1 * n2
for v in range(q):
    j = v % n2
    if j==0 and v!=0 and i<n1 and v!=q:
        for k in range(len(a[i])):
            print(r)