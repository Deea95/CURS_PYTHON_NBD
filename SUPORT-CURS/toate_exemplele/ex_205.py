# 10.8.6 Ex. (205) – One function for any to any conversion and input type detection
def convert_to(h, a):
    n = len(a)
    t = sum(len(element) for element in a) / n
    if t == 1:
        q = 'txt'
    elif 2 <= t < 3:
        q = 'hex'
    elif 3 <= t < 4:
        q = 'dec'
    else:
        q = 'bin'
    if q == h:
        return a
    for i in range(len(a)):
        conversion_type = q + '_' + h
        if conversion_type == 'txt_hex':
            a[i] = f
            ormat(ord(a[i]), 'x').zfill(2)
        elif conversion_type == 'dec_hex':
            a[i] = f
            ormat(chr(a[i]), 'x').zfill(2)
        elif conversion_type == 'txt_bin':
            a[i] = f
            ormat(ord(a[i]), 'b')
        elif conversion_type == 'txt_dec':
            a[i] = o
            rd(a[i])
        elif conversion_type == 'hex_dec':
            a[i] = o
            rd(chr(int(a[i], 16)))
        elif conversion_type == 'bin_dec':
            a[i] = o
            rd(chr(int(a[i], 2)))
        elif conversion_type == 'hex_txt':
            a[i] = c
            hr(int(a[i], 16))
        elif conversion_type == 'bin_txt':
            a[i] = c
            hr(int(a[i], 2))
        elif conversion_type == 'dec_txt':
            a[i] = c
            hr(a[i])
        elif conversion_type == 'dec_bin':
            a[i] = format(ord(chr(a[i])), 'b')
        elif conversion_type == 'hex_bin':
            a[i] = format(int(a[i], 16), 'b')
        elif conversion_type == 'bin_hex':
            a[i] = format(int(a[i], 2), 'x')
    return a


a = list("☁Ѐ.~ text")
print('Array a =', a)
print(convert_to('bin', a))
Array
a = ☁, Ѐ,., ~,, t, e, x, t
Separate
functions
for one to one conversions are important pieces of code that can be
