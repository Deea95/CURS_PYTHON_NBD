# 9.2.5 Ex. (162) – Complex string to object (II) - nested access by reference
txt = '{"v1":["a","b","c"],"v2":' + \
'[[0,1,0],[1,1,1],[0,1,0]]' + \
',"v3":{"c1":["a","b","c"]' + \
',"c2":[[0,1,0],[1,1,1],[0' + \
',1,0]],"c3":42}}'
import json

obj = json.loads(txt)

a = obj['v1']
b = obj['v2']
c = obj['v3']

print(a)
print(b)
print(c['c1'])
print(c['c2'])
print(c['c3'])
