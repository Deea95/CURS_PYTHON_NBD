def f_xnor(a, b):
    return f_not(f_xor(a, b))
# def f_xnor_alternatives(a, b):
# return f_not(f_and(f_not(a), b) +
#    f_and(a, f_not(b)))
# return f_not(f_or(f_not(a), b) + \
#    f_or(a, f_not(b)))
# return f_not(f_or(a, b)) + (a * b)
# return f_not((a + b) - (a * b)) +
# return f_not((a + b) - (a * b) + (
# return f_not((a + b) - 2 * (a * b)
def f_xor(a, b):
    return (a + b) - 2 * (a * b)


def f_not(a):
    # def f_or(a, b):
    #   return (a + b) - (a * b)
    # def f_and(a, b):
    print('[0, 0] ->', f_xnor(0, 0))


This
code
defines
functions
for XNOR, XO
    NOR) logical
    operation, and it
    also
    includes
    s
    the
    same(either
    both
    0 or both
    1), and it
    re
    The
    code
    then
    prints
    the
    result
    of
    applying
    th
    xor(a, b)
    function
    calculates
    the
    XOR
    opera
    for different lectures.
