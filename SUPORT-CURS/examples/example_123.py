def SMC(m):
    r = "\n"
    for i in range(len(m)):
        for j in range(len(m[i])):
            a = [
            b = [
            c = [
            n = len(a)
            m = len(a[0])
            for i in range(n):
                for j in range(m):
                    if b[i][j ] ==0 :
                    elif b[i][j ] ==1:
                    elif b[i][j ] ==2:
                    elif b[i][j ] ==3:
                    elif b[i][j ] ==4:
                    elif b[i][j ] ==5:
                    elif b[i][j ] ==6:
                    elif b[i][j ] ==7:
                    elif b[i][j ] ==8:
                    elif b[i][j ] ==9:
                        if c[i][j ] <=a[i][j]:
                            print(SMC(c))