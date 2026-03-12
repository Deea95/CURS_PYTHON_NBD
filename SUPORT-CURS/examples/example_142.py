a = [1, 2, 3, 4, 5]
t = 0
def c1(t, a):
    def c2(t, a):
        def c3(t, a):
            s = 1
            def c4(t, a):
                def c5(t, a):
                    for i in a:
                        b = c1(t, a)
                        print(b)