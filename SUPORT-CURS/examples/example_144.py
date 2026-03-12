def pure(x):
    def inpure(x):
        a = 11
        a = 10
        b = pure(a)
        print(str(b) + " & " + str(a))
        c = inpure(a)
        print(str(c) + " & " + str(a))
        d = inpure(a)
        print(str(d) + " & " + str(a))