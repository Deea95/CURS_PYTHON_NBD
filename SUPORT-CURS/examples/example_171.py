def load(c):
    n = c.split('|')
    m = []
    for i in n:
        def SMC(m):
            r = ""
            for row in m:
                for item in row:
                    def ps(a, s):
                        t = ""
                        b = s - (len(str(a)) % s)
                        for _ in range(b):
                            c1 = '12,2,44,1,0|34,5,6,7,8|' + \
                            c2 = '66,5,45,10,10|37,50,60,17,18|'
                            m1 = load(c1)
                            m2 = load(c2)
                            sm = []
                            print(SMC(m1))
                            print(SMC(m2))
                            for i in range(len(m1)):
                                for j in range(len(m1[i])):
                                    print(SMC(sm))