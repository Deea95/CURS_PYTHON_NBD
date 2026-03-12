txt = '{"v1":["a","b","c"],"v2":' + \
obj = json.loads(txt)
print(obj['v1'][1])
print(obj['v2'][0][1])
print(obj['v3']['c2'])
print(obj['v3']['c2'][1][1])