# 10.8.5 Ex. (204) – Multiple functions for any to any conversion
def txt_hex(a):
    for i, char in enumerate(a):
        a[i] = format(ord(char), 'x')
        a[i] = a[i] if len(a[i]) >= 2 else "0" + a[i]
    return a


def txt_bin(a):
    for i, char in enumerate(a):
        a[i] = format(ord(char), 'b').zfill(8)
    return a


def txt_dec(a):
    for i, char in enumerate(a):
        a[i] = ord(char)
    return a


def hex_txt(a):
    for i, char in enumerate(a):
        a[i] = chr(int(char, 16))
    return a


def hex_bin(a):
    for i, char in enumerate(a):
        a[i] = bin(int(char, 16))[2:].zfill(8)
    return a


def hex_dec(a):
    a = hex_txt(a[:])
    for i, char in enumerate(a):
        a[i] = ord(char)
    return a


def bin_hex(a):
    for i, char in enumerate(a):
        a[i] = format(int(char, 2), 'x')
    return a


def bin_txt(a):
    for i, char in enumerate(a):
        a[i] = chr(int(char, 2))
    return a


def bin_dec(a):
    a = bin_txt(a[:])
    for i, char in enumerate(a):
        a[i] = ord(char)
    return a


def dec_hex(a):
    a = dec_txt(a[:])
    return txt_hex(a)


def dec_txt(a):
    for i, char in enumerate(a):
        a[i] = chr(char)
    return a


def dec_bin(a):
    a = dec_txt(a[:])
    return txt_bin(a)


a = list("☁Ѐ.~ text")
print('Array a =', a)
print('txt_hex =', txt_hex(a[:]))
print('hex_bin =', hex_bin(txt_hex(a[:])))
print('bin_dec =', bin_dec(txt_bin(a[:])))
print('dec_txt =', dec_txt(txt_dec(a[:])))
print('txt_bin =', txt_bin(a[:]))
print('bin_hex =', bin_hex(txt_bin(a[:])))
print('hex_dec =', hex_dec(txt_hex(a[:])))
print('dec_bin =', dec_bin(txt_dec(a[:])))
print('bin_txt =', bin_txt(txt_bin(a[:])))
print('txt_dec =', txt_dec(a[:]))
print('dec_hex =', dec_hex(txt_dec(a[:])))
print('hex_txt =', hex_txt(txt_hex(a[:])))
Array
a = ☁, Ѐ,., ~,, t, e, x, t
txt_hex = 2601, 400, 2
e, 7
e, 20, 74, 65, 78, 74
hex_bin = 10011000000001, 10000000000, 101110, 1111110,
bin_dec = 9729, 1024, 46, 126, 32, 116, 101, 120, 116
dec_txt = ☁, Ѐ,., ~,, t, e, x, t
txt_bin = 10011000000001, 10000000000, 101110, 1111110,
bin_hex = 2601, 400, 2
e, 7
e, 20, 74, 65, 78, 74
hex_dec = 9729, 1024, 46, 126, 32, 116, 101, 120, 116
dec_bin = 10011000000001, 10000000000, 101110, 1111110,
bin_txt = ☁, Ѐ,., ~,, t, e, x, t
txt_dec = 9729, 1024, 46, 126, 32, 116, 101, 120, 116
dec_hex = 2601, 400, 2
e, 7
e, 20, 74, 65, 78, 74
hex_txt = ☁, Ѐ,., ~,, t, e, x, t
