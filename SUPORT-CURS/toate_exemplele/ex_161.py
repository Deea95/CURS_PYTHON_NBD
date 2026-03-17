# 9.2.4 Ex. (161) – Complex string to object (I) - direct nested access
txt = '{"v1":["a","b","c"],"v2":' + \ b
'[[0,1,0],[1,1,1],[0,1,0]]' + \ 1
',"v3":{"c1":["a","b","c"]' + \ 0, 1, 0, 1, 1, 1, 0, 1, 0
',"c2":[[0,1,0],[1,1,1],[0' + \ 1
',1,0]],"c3":42}}'
obj = json.loads(txt)
print(obj['v1'][1])
print(obj['v2'][0][1])
print(obj['v3']['c2'])
print(obj['v3']['c2'][1][1])
