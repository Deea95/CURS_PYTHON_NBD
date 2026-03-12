def permute(s, a, b):
    if len(s) == 0:
        for i in range(len(s)):
            c = s[i]
            l = s[:i] # left part.
            r = s[i + 1:] # right part.
            q = l + r
            s = 'ABC'
            a = ''
            b = []
            print(b)