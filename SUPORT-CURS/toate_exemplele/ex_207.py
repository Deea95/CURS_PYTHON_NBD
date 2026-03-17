# 11.1.1 Ex. (207) – Spectral forecast for signals in Python.

# Spectral forecast for signals in Python.

A = '10.3,23.4,44.8,63.2,44.1,35.1,46.5,62.6,50.4'
B = '18.8,43.1,52.2,45.5,46.8,46.6,67.9,66.3,70.4'
M = ''

tA = A.split(',')
tB = B.split(',')

maxA = max(map(float, tA))
maxB = max(map(float, tB))
max_value = max(maxA, maxB)

d = 33

for i in range(len(tA)):
    v=((d/maxA)*float(tA[i]))+(((max_value-d)/maxB)*float(tB[i]))
    M += '{:.2f}'.format(v)
    if i < len(tA)-1:
        M += ','
print('Signal A:' + A)
print('Max(A[i]):' + str(maxA))
print('Signal M:' + M)
print('Signal B:' + B)
print('Max(B[i]):' + str(maxB))