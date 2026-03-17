# 5.1.43Ex. (83) – Horizontal chart from ASCII characters
a = [5, 1, 8, 4, 6, 2, 8, 9]

c = '#'  #####
t = ''  #
########
n = len(a)
####
######
for i in range(n):
    ##
    for k in range(a[i]):
        ########
        t += c
        #########
    t += '\n'
print(t)
