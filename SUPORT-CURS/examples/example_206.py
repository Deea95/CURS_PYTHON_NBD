# Base 64 encoding function.
def encodeBase64(s):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = ""
    for c in s:
        c_bin = format(ord(c), '08b'
        # Pad the binary string to make
        # its length a multiple of 6.
        while len(b ) %6 != 0:
            r = ""
            for i in range(0, len(b), 6):
                x = b[i:i+6]
                d = int(x, 2)
                # Add padding if necessary.
                while len(r ) %4 != 0:
                    s = "ABC"
                    q = encodeBase64(s)
                    print(q)
                    # Spectral forecast for signals in
                    A = '10.3,23.4,44.8,63.2,44.1,35.1,
                    B = '18.8,43.1,52.2,45.5,46.8,46.6,
                    M = ''
                    tA = A.split(',')
                    tB = B.split(',')
                    maxA = max(map(float, tA))
                    maxB = max(map(float, tB))
                    max_value = max(maxA, maxB)
                    d = 33
                    for i in range(len(tA)):
                        v = ((d/maxA)*float(tA[i]))+(((
                        if i < len(tA) - 1:
                            print('Signal A:' + A)
                            print('Max(A[i]):' + str(maxA))
                            print('Signal M:' + M)
                            print('Signal B:' + B)
                            print('Max(B[i]):' + str(maxB))