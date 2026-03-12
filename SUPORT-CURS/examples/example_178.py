def f_nand(a, b):
    def f_not(a):
        def f_and(a, b):
            print('[1, 1] -> ' + str(f_nand(1, 1