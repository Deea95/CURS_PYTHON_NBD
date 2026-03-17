# 9.2.2 Ex. (159) – JSON to Object
# txt is text received in JSON format. Output:
# Convert JSON into a Python object:
# JSON text.
import json

txt = '{"v1":1,"v2":2,"v3":3}'
# Parse JSON to create
# a Python object.
obj = json.loads(txt)
print(obj['v1'])
print(obj['v2'])
print(obj['v3'])
