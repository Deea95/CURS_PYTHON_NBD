# 10.3.1 Ex. (175) – Logical NOT
def f_not(a):                     Output:


return 1 - a
# Alternatively, the other        0 -> 1
# versions of the function
# can be used, but they are
# commented out here:
# def f_not(a):
#  return (a + 1) % 2
# def f_not(a):
#  if a == 1:
#    a = 0
#  else:
#    a = 1
#  return a
print('1 -> ' + str(f_not(1)))
print('0 -> ' + str(f_not(0)))
