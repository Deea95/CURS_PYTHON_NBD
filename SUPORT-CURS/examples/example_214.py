# Local sequence alignment
# algorithm and the layout.
def f(a1, a2):
    if a1 == a2:
    else:
        Match = 2
        Mismatch = -1
        gap = -2
        s0 = '1100111111111001'
        s1 = '00000011111111100000'
        AA = ""
        AM = ""
        AB = ""
        e = ' '
        m = []
        s = []
        MMax = 0
        MMin = 0
        x = 0
        y = 0
        # Matrix initialization and completio
        s = [list(s0), list(s1)]
        n_0 = len(s[0]) + 1
        n_1 = len(s[1]) + 1
        for i in range(n_0):
            for j in range(n_1):
                if i == 1 and j > 1:
                    if j == 1 and i > 1:
                        if i > 1:
                            if j > 1:
                                if i > 1 and j > 1:
                                    A = m[i-1][j-1]+f(m[i][0]
                                    B = m[i-1][j]+gap
                                    C = m[i][j-1]+gap
                                    D = 0
                                    if m[i][j ] >MMax:
                                        MMax = m[i][j]
                                        x = i
                                        y = j
                                        if m[i][j ] <MMin:
                                            MMin = m[i][j]
                                            # Traceback & text alignment.
                                            i = x
                                            j = y
                                            while i >= 2 or j >= 2:
                                                Ai = m[i][0]
                                                Bj = m[0][j]
                                                A = m[i-1][j-1 ] +f( Ai, Bj)
                                                B = m[i-1][j ] +g ap
                                                C = m[i][j-1 ] +g ap
                                                if i >= 2 and j >= 2 and m[i][j ]
                                                AA = Ai + AA
                                                AB = Bj + AB
                                                if Ai == Bj:
                                                    AM = '|' + AM
                                                else:
                                                    AM = e + AM
                                                else:
                                                    if i >= 2 and m[i][j] == B:
                                                        AA = Ai + AA
                                                        AB = '-' + AB
                                                        AM = e + AM
                                                    else:
                                                        AA = '-' + AA
                                                        AB = Bj + AB
                                                        AM = e + AM
                                                        r1 = i - 1
                                                        r2 = j - 1
                                                        if m[i][j] <= 0:
                                                            # Layout.
                                                            tM = ''
                                                            tS = ''
                                                            # Check the end.
                                                            # Check the beginning.
                                                            AA = s0[:r1] + AA
                                                            AB = s1[:r2] + AB
                                                            if r1 > r2:
                                                                v = r1 - r2
                                                                AB = tS + AB
                                                                AM = tM + AM
                                                            else:
                                                                v = r2 - r1
                                                                AA = tS + AA
                                                                AM = tM + AM
                                                                # Print the alignment.
                                                                print(AA)
                                                                print(AM)
                                                                print(AB)
                                                                print the matrix obtained after the mutation.
                                                                prints the accumulated string z to the consol
                                                                for the next iteration. The values in v[0] ar
                                                                print the content of a file. The function take
                                                                printed. This function is then called with th
                                                                for power system analysis education and rese
                                                                for rapid prototyping, in IEEE 28th Internati