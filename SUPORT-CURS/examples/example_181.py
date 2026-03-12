def f_xnor(a, b):
    # The commented-out lines represent
    # alternative implementations of XNO
    # def f_xnor_alternatives(a, b):
        # return f_not(f_and(f_not(a), b) +
        # f_and(a, f_not(b)))
        # return f_not(f_or(f_not(a), b) + \
        # f_or(a, f_not(b)))
        # return f_not(f_or(a, b)) + (a * b)
        # return f_not((a + b) - (a * b)) +
        # return f_not((a + b) - (a * b) + (
        # return f_not((a + b) - 2 * (a * b)
        def f_xor(a, b):
            def f_not(a):
                # The OR and AND functions are
                # commented out also:
                    # def f_or(a, b):
                        # return (a + b) - (a * b)
                        # def f_and(a, b):
                            # return a * b
                            print('[0, 0] ->', f_xnor(0, 0))
                            for different lectures.