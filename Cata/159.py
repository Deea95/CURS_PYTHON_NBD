
import json

txt = '{"v1":1,"v2":2,"v3":3}'

obj = json.loads(txt)
print(obj['v1'])
print(obj['v2'])
print(obj['v3'])