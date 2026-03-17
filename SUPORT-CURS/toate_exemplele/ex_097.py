# 7.1.3 Ex. (97) – Show matrix content
m = [Output:
[2, 4, 6],
[3, 5, 6], 2
4
6
[3, 5, 4]
3
5
6
]                       3
5
4
r = ""
for i in range(len(m)):
    r += "\n"
    for j in range(len(m[i])):
        r += str(m[i][j]) + " "
print(r)
