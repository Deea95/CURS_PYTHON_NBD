# 10.1.1 Ex. (165) – Strings to 1D arrays (I)
def main_app():

    a = "10|13|55|56|1|3|123"
    b = "45|33|55|0|1|22|127"

    aa = a.split("|")
    bb = b.split("|")
    cc = []

    for i in range(len(aa)):
        cc.append(daniela(i, aa, bb))
    print(cc)


def daniela(i, aa, bb):
    return int(aa[i]) * int(bb[len(aa) - 1 - i])

d = main_app()
