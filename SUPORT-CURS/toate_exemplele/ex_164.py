# 9.2.7 Ex. (164) – Make a matrix from parts of an object
import json

txt = '{"v1":["a","b","c"],"v2":' + \
      '[[0,1,0],[1,1,1],[0,1,0]]' + \
      ',"v3":{"c1":["a","b","c"]' + \
      ',"c2":[[0,1,0],[1,1,1],[0' + \
      ',1,0]],"c3":42}}'

obj = json.loads(txt)
a = []

for i in range(len(obj['v3']['c2'])):
    a.append([])
    for j in range(len(obj['v3']['c2'][i])):
        a[i].append(obj['v3']['c2'][i][j])

def smc(m):
    r = ''
    for i in range(len(m)):
        for j in range(len(m[i])):
            r += str(m[i][j]) + " "
        r += "\n"
    return r

print(smc(a))
