# 10.1.2 Ex. (166) – Strings to 1D arrays (II)
def main_app():             Output:


a = "10|13|55|56|1|3|123"
b = "45|33|55|0|1|22|127"
1270, 286, 55, 0, 55, 99, 5535
aa = list(map(int, a.split("|")))
bb = list(map(int, b.split("|")))
cc = []
for i in range(len(aa)):
    cc.append(sebastian(i, aa, bb))
return cc


def sebastian(i, aa, bb):
    return aa[i] * bb[len(aa) - 1 - i]


d = main_app()
print(d)
