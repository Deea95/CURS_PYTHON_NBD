m = [
a = [
for i in range(len(m)):
    for j in range(len(m[i])):
        if not a[2][j]:
            if not a[3][i]:
                if a[0][j] < m[i][j]:
                    if a[1][i] < m[i][j]:
                        if a[2][j] > m[i][j]:
                            if a[3][i] > m[i][j]:
                                print('C Max =', a[0])
                                print('R Max =', a[1])
                                print('C Min =', a[2])
                                print('R Min =', a[3])
                                # or an optimised version:
                                    m = [
                                    a = [
                                    for i in range(len(m)):
                                        for j in range(len(m[i])):
                                            print('C Max =', a[0])
                                            print('R Max =', a[1])
                                            print('C Min =', a[2])
                                            print('R Min =', a[3])