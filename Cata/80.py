a = "0|13|55|56|1|30|123"
b = "5|33|55|90|1|22|127"
aa = a.split("|")
bb = b.split("|")
cc =[] 

for i in range(len(aa)):
    cc.append(int(aa[i]) + int(bb[i]))

print(cc)