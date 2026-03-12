            def txt_hex(a):
              for i, char in enumerate(a):
                a[i] = format(ord(char), 'x'
                a[i] = a[i] if len(a[i]) >=
            def txt_bin(a):
              for i, char in enumerate(a):
                a[i] = format(ord(char), 'b'
            def txt_dec(a):
              for i, char in enumerate(a):
                a[i] = ord(char)
            def hex_txt(a):
              for i, char in enumerate(a):
                a[i] = chr(int(char, 16))
            def hex_bin(a):
              for i, char in enumerate(a):
                a[i] = bin(int(char, 16))[2:
           def hex_dec(a):
              a = hex_txt(a[:])
              for i, char in enumerate(a):
                a[i] = ord(char)
           def bin_hex(a):
              for i, char in enumerate(a):
                a[i] = format(int(char, 2),
           def bin_txt(a):
              for i, char in enumerate(a):
                a[i] = chr(int(char, 2))
           def bin_dec(a):
              a = bin_txt(a[:])
              for i, char in enumerate(a):
                a[i] = ord(char)
           def dec_hex(a):
              a = dec_txt(a[:])
              return txt_hex(a)
           def dec_txt(a):
              for i, char in enumerate(a):
                a[i] = chr(char)
           def dec_bin(a):
              a = dec_txt(a[:])
              return txt_bin(a)
           a = list("☁Ѐ.~ text")
           print('Array a =', a)
           print('txt_hex =', txt_hex(a[:]))
           print('hex_bin =', hex_bin(txt_hex(a
           print('bin_dec =', bin_dec(txt_bin(a
           print('dec_txt =', dec_txt(txt_dec(a
           print('txt_bin =', txt_bin(a[:]))
           print('bin_hex =', bin_hex(txt_bin(a
           print('hex_dec =', hex_dec(txt_hex(a
           print('dec_bin =', dec_bin(txt_dec(a
           print('bin_txt =', bin_txt(txt_bin(a
           print('txt_dec =', txt_dec(a[:]))
           print('dec_hex =', dec_hex(txt_dec(a
           print('hex_txt =', hex_txt(txt_hex(a
            Array a = ☁,Ѐ,.,~, ,t,e,x,t
            txt_hex = 2601,400,2e,7e,20,74,6
            hex_bin = 10011000000001,1000000
            bin_dec = 9729,1024,46,126,32,11
            dec_txt = ☁,Ѐ,.,~, ,t,e,x,t
            txt_bin = 10011000000001,1000000
            bin_hex = 2601,400,2e,7e,20,74,6
            hex_dec = 9729,1024,46,126,32,11
            dec_bin = 10011000000001,1000000
            bin_txt = ☁,Ѐ,.,~, ,t,e,x,t
            txt_dec = 9729,1024,46,126,32,11
            dec_hex = 2601,400,2e,7e,20,74,6
            hex_txt = ☁,Ѐ,.,~, ,t,e,x,t
        hex(a) function converts each character in t
        Next, the txt dec(a) function, conversely, con
        Next, the hex txt(a) function converts each
        using chr() to get the character. Next, the h
        bin hex(a) function converts each binary va
        bin txt(a) function converts each binary valu
        the bin dec(a) function closes the circle of
        prints the results for each conversion. This