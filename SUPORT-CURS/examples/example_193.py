def permute(s, a, b):
    if len(s) == 0:
        b.append(a)
    for i in range(len(s)):
        c = s[i]
        l = s[:i]  # left part.
        r = s[i + 1:]  # right part.
        q = l + r
        permute(q, a + c, b)


s = 'ABC'
a = ''
b = []
permute(s, a, b)
print(b)
function
a
few
statements
allow
for the per
    and r(the
    characters
    to
    the
    right
    of
    c).Also,
    console
    for the user inspection, which contai
    tion, statistics
    serves as a
    crucial
    tool
    for bo
