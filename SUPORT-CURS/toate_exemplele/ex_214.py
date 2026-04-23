# Exemplul 214 - Show similarities between two strings by sequence alignment
# Local sequence alignment algorithm (Smith-Waterman approach)

def f(a1, a2):
    if a1 == a2:
        return Match
    else:
        return Mismatch


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

# Matrix initialization and completion.
s = [list(s0), list(s1)]
n_0 = len(s[0]) + 1
n_1 = len(s[1]) + 1

for i in range(n_0):
    m.append([])
    for j in range(n_1):
        m[i].append(0)

        if i == 1 and j > 1:
            m[i][j] = m[i][j - 1] + gap
        if j == 1 and i > 1:
            m[i][j] = m[i - 1][j] + gap

        if i > 1:
            m[i][0] = s[0][i - 2]
        if j > 1:
            m[0][j] = s[1][j - 2]

        if i > 1 and j > 1:
            A = m[i - 1][j - 1] + f(m[i][0], m[0][j])
            B = m[i - 1][j] + gap
            C = m[i][j - 1] + gap
            D = 0
            m[i][j] = max(A, B, C, D)

            if m[i][j] > MMax:
                MMax = m[i][j]
                x = i
                y = j
            if m[i][j] < MMin:
                MMin = m[i][j]

# Traceback & text alignment.
i = x
j = y
r1 = 0
r2 = 0

while i >= 2 or j >= 2:
    Ai = m[i][0]
    Bj = m[0][j]

    # Verificăm din ce direcție a venit scorul maxim
    A = m[i - 1][j - 1] + f(Ai, Bj)
    B = m[i - 1][j] + gap
    C = m[i][j - 1] + gap

    if i >= 2 and j >= 2 and m[i][j] == A:
        AA = Ai + AA
        AB = Bj + AB
        AM = ('|' if Ai == Bj else e) + AM
        i -= 1
        j -= 1
    elif i >= 2 and m[i][j] == B:
        AA = Ai + AA
        AB = '-' + AB
        AM = e + AM
        i -= 1
    else:
        AA = '-' + AA
        AB = Bj + AB
        AM = e + AM
        j -= 1

    r1 = i - 1
    r2 = j - 1
    if m[i][j] <= 0:
        break

# Layout & Final adjustment
tM = ''
tS = ''

# Check the end.
AA += s0[x - 1:n_0 - x]
AB += s1[y - 1:n_1 - y]

# Check the beginning.
AA = s0[:r1] + AA
AB = s1[:r2] + AB

if r1 > r2:
    v = r1 - r2
    AB = (e * v) + AB
    AM = (e * (v + r2)) + AM
else:
    v = r2 - r1
    AA = (e * v) + AA
    AM = (e * (v + r1)) + AM

# Print the alignment.
print(AA)
print(AM)
print(AB)
matches = 0
total = 0

# # var 1
# matches = 0
# aligned_positions = len(AA)
#
# for i in range(aligned_positions):
#     if AA[i] == AB[i] and AA[i] != '-' and AB[i] != '-':
#         matches += 1
#
# similarity = (matches / aligned_positions) * 100
# print(f"Similarity: {similarity:.2f}%")

# sau var 2
matches = 0
total = 0

for i in range(len(AA)):
    if AA[i] != '-' or AB[i] != '-':
        total += 1
        if AA[i] == AB[i]:
            matches += 1

similarity = (matches / total) * 100
print(f"Similarity: {similarity:.2f}%")