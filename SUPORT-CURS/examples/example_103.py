a = [
d = 0
n = len(a)
m = len(a[0])
i = 0
while i < n:
    j = 0
    while j < m:
        print(a[i][m-j-1])
        print('---\n' + str(d))
        # or a second version:
            a = [
            d = 0
            n = len(a)
            m = len(a[0])
            i = 0
            for j in range(m):
                print(a[i][m-j-1])
                print('---\n' + str(d))
                print statement that displays a line containin