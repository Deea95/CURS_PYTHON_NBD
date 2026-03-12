txt = '{"v1":["a","b","c"],"v2":' + \
obj = json.loads(txt)
a = obj['v1']
b = obj['v2']
c = obj['v3']
print(a)
print(b)
print(c['c1'])
print(c['c2'])
print(c['c3'])