# 9.2.6 Ex. (163) – Make 1D array from parts of an object
txt = '{"v1":["a","b","c"],"v2":' + \ a, b, c
'[[0,1,0],[1,1,1],[0,1,0]]' + \
',"v3":{"c1":["a","b","c"]' + \
',"c2":[[0,1,0],[1,1,1],[0' + \
',1,0]],"c3":42}}'
obj = json.loads(txt)
a = []
for i in obj['v3']['c1']:
    a.append(i)
print(a)
