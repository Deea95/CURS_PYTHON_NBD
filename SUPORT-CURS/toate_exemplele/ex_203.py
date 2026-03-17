# 10.8.4 Ex. (203) – A txt to hex in a function that receives an as argument
# txt to hex by in a function  Output:
# that recives a as argument
def hexify(a):
    for i in range(len(a)):
        a[i] = format(ord(a[i]), 'x')
        a[i] = a[i] if len(a[i]) >= 2 else "0" + a[i]
    return a


a = list(".~ text")
print(hexify(a))
