# 10.8.7 Ex. (206) – Base64 encoding function
# Base 64 encoding function.      Output:
def encodeBase64(s):              QUJD


a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
    b = ""
for c in s:
    c_bin = format(ord(c), '08b')
    b += c_bin
    # Pad the binary string to make
# its length a multiple of 6.
while len(b) % 6 != 0:
    b += "0"
r = ""
for i in range(0, len(b), 6):
    x = b[i:i + 6]
    d = int(x, 2)
    r += a[d]
    # Add padding if necessary.
while len(r) % 4 != 0:
    r += "="
return r
s = "ABC"
q = encodeBase64(s)
print(q)
